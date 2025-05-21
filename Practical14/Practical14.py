import os
import xml.dom.minidom
import xml.sax
import datetime

file_path = r"C:\Users\ASUS\Desktop\ZJE\IBI1\IBI1_2024-25\Practical14\go_obo.xml"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

def remove_bom(file_path):
    with open(file_path, "rb") as file:
        content = file.read()
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
    with open(file_path, "wb") as file:
        file.write(content)

remove_bom(file_path)

def parse_go_obo_dom(file_path):
    start_time = datetime.datetime.now()
    doc = xml.dom.minidom.parse(file_path)
    terms = doc.getElementsByTagName("term")

    ontology_results = {
        "molecular_function": {"term_id": None, "is_a_count": 0},
        "biological_process": {"term_id": None, "is_a_count": 0},
        "cellular_component": {"term_id": None, "is_a_count": 0}
    }

    for term in terms:
        term_id = term.getElementsByTagName("id")[0].firstChild.data
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data
        is_a_elements = term.getElementsByTagName("is_a")

        if namespace in ontology_results:
            if len(is_a_elements) > ontology_results[namespace]["is_a_count"]:
                ontology_results[namespace]["term_id"] = term_id
                ontology_results[namespace]["is_a_count"] = len(is_a_elements)

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    return ontology_results, duration

class GOTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.current_term = {}
        self.ontology_results = {
            "molecular_function": {"term_id": None, "is_a_count": 0},
            "biological_process": {"term_id": None, "is_a_count": 0},
            "cellular_component": {"term_id": None, "is_a_count": 0}
        }

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "term":
            self.current_term = {"is_a_count": 0} 

    def endElement(self, tag):
        if tag == "term":
            namespace = self.current_term.get("namespace", "")
            if namespace in self.ontology_results:
                if self.current_term["is_a_count"] > self.ontology_results[namespace]["is_a_count"]:
                    self.ontology_results[namespace]["term_id"] = self.current_term["id"]
                    self.ontology_results[namespace]["is_a_count"] = self.current_term["is_a_count"]
            self.current_term = {}

    def characters(self, content):
        if self.current_tag == "id":
            self.current_term["id"] = content
        elif self.current_tag == "namespace":
            self.current_term["namespace"] = content
        elif self.current_tag == "is_a":
            if "is_a_count" not in self.current_term:
                self.current_term["is_a_count"] = 0
            self.current_term["is_a_count"] += 1

def parse_go_obo_sax(file_path):
    start_time = datetime.datetime.now()
    handler = GOTermHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    return handler.ontology_results, duration

def print_results(results, duration, api_name):
    print(f"Results using {api_name}:")
    for ontology, data in results.items():
        print(f"{ontology.capitalize().replace('_', ' ')}:")
        print(f"Term ID: {data['term_id']}")
        print(f"Number of <is_a> elements: {data['is_a_count']}")
        print()
    print(f"{api_name} Time Taken: {duration.total_seconds()} seconds")
    print("-" * 40)

dom_results, dom_duration = parse_go_obo_dom(file_path)
print_results(dom_results, dom_duration, "DOM API")
sax_results, sax_duration = parse_go_obo_sax(file_path)
print_results(sax_results, sax_duration, "SAX API")
if dom_duration < sax_duration:
    print("DOM API was faster.")
elif sax_duration < dom_duration:
    print("SAX API was faster.")
else:
    print("Both APIs had the same performance.")