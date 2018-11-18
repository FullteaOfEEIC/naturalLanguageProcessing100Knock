import xml.etree.ElementTree as ET

nlp = []

marks=[".",",",";",":","!","?"]

tree = ET.parse("nlp.xml")
root = tree.getroot()

if __name__=="__main__":
    document = root[0]
    scentences = document[1]
    for scentence in scentences:
        tokens = scentence[0]
        for token in tokens:
            for e in token:
                if e.tag=="word" and (e.text not in marks):
                    print(e.text)
        print()
