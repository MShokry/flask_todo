import csv
import json

class Node(object):
    def __init__(self, name, size=None, extra=None):
        self.name = name
        self.children = []
        self.size = size
        self.extra = extra

    def child(self, cname, size=None, extra=None):
        child_found = [c for c in self.children if c.name == cname]
        if not child_found:
            _child = Node(cname, size, extra)
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child

    def as_dict(self):
        res = {'name': self.name}
        if self.size is None:
            res['children'] = [c.as_dict() for c in self.children]
        else:
            res['size'] = self.size

        if self.extra:
            res.update(self.extra)

        return res

root = Node('Cars')

with open('cars.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        car, model = row
        root.child(car, extra={'type' : 'car'}) \
            .child(model, extra={'type' : 'model'}) \

print (json.dumps(root.as_dict(), indent=4,ensure_ascii = False))
with open('cars.json', 'w') as outfile:
    json.dump(root.as_dict(), outfile,ensure_ascii = False)
