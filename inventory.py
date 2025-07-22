from objects import OBJECTS


class Inventory:

    def __init__(self, objects=None):
        if objects:
            if isinstance(objects, Inventory):
                objects = objects.objects
            self.objects = objects
        else:
            self.objects = {}

    def add(self, obj):
        if obj in self.objects:
            self.objects[obj] += 1
        else:
            self.objects[obj] = 1

    def remove(self, obj):
        if obj not in self.objects:
            raise KeyError()
        self.objects[obj] -= 1
        if self.objects[obj] == 0:
            del self.objects[obj]

    def count(self, obj):
        return self.objects.get(obj, 0)

    def __str__(self):
        if not self:
            return "ничего"
        tmp = []
        for k, v in sorted(self.objects.items()):
            if v == 1:
                tmp.append(k)
            else:
                tmp.append("{} x{}".format(k, v))
        return ", ".join(tmp)

    def update(self, inv):
        for obj, count in inv.objects.items():
            if obj not in self.objects:
                self.objects[obj] = 0
            self.objects[obj] += count

    def __contains__(self, key):
        return key in self.objects

    def action(self, game, player, action):
        obj, action = action.split()
        if obj not in self.objects:
            raise KeyError()
        is_used = OBJECTS[obj].action(game, player, action)
        if is_used:
            self.remove(obj)
        return is_used is not None

    def __bool__(self):
        return bool(self.objects)

    def get_excess(self, other):
        res = {}
        for obj, new_cnt in other.objects.items():
            old_cnt = self.objects.get(obj, 0)
            if new_cnt > old_cnt:
                res[obj] = new_cnt - old_cnt
        return type(self)(res)
