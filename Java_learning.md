LinkedList &#60;T&#62; Methods
* void add(index, object): Insert object at the index.
* boolean add(object): add object to the end of list
* void addFirst(object): Add object to the beginning of list
* object remove(index): remove object at index and return the reference.
* int size(): return the number of objects in list


Stack &#60;T&#62; Methods
* void push(object): push object to the stack
* object pop(): remove object at the top of stack and return it.
* object peek(): return object at the top of stack without removing it.
* boolean empty(): return true if stack is empty


Java how to create comparator efficiently.
For instance, Interval objects have start attributes.

1) Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a, Interval b){
                return a.start - b.start;
            }
        });

2) Using Java 8 Lambda:
   intervals.sort((Interval x, Interval y) -> x.start - y.start);


