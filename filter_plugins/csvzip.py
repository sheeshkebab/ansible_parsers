class FilterModule(object):
     def filters(self):
         return { 'csvzip': lambda _list1, _list2: { k: v for k, v in zip(_list1, _list2) }  }
         #return { 'makedict': lambda _val, _list: { k: _val for k in _list }  }
