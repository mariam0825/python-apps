class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    // Add a node to the end
    append(data) {
        let newNode = new Node(data);

        if (this.head == null) {
            this.head = newNode;
        } else {
            let current = this.head;

            while (current.next != null) {
                current = current.next;
            }

            current.next = newNode;
        }

        this.size++;
    }

    // Add a node to the beginning
    prepend(data) {
        let newNode = new Node(data);

        if (this.head == null) {
            this.head = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }

        this.size++;
    }

    // Insert a node at a specific position
    insertAt(data, index) {
        let newNode = new Node(data);

        // Empty list
        if (this.head == null) {
            if (index == 0) {
                this.head = newNode;
                this.size++;
            }
            return;
        }

        // Insert at beginning
        if (index == 0) {
            this.prepend(data);
            return;
        }

        let current = this.head;
        let counter = 0;

        while (counter < index - 1 && current.next != null) {
            current = current.next;
            counter++;
        }

        newNode.next = current.next;
        current.next = newNode;

        this.size++;
    }

    // Remove the last node
    pop() {
        if (this.head == null) {
            return null;
        }

        // Only one node
        if (this.head.next == null) {
            let removedData = this.head.data;
            this.head = null;
            this.size--;
            return removedData;
        }

        let current = this.head;

        while (current.next.next != null) {
            current = current.next;
        }

        let removedData = current.next.data;

        current.next = null;
        this.size--;

        return removedData;
    }

    // Remove a node at a specific position
    removeAt(index) {
        if (this.head == null) {
            return null;
        }

        // Remove first node
        if (index == 0) {
            let removedData = this.head.data;
            this.head = this.head.next;
            this.size--;

            return removedData;
        }

        let current = this.head;
        let counter = 0;

        while (counter < index - 1 && current.next != null) {
            current = current.next;
            counter++;
        }

        if (current.next == null) {
            return null;
        }

        let removedData = current.next.data;

        current.next = current.next.next;
        this.size--;

        return removedData;
    }

    // Get a value at a specific position
    get(index) {
        let current = this.head;
        let counter = 0;

        while (current != null) {
            if (counter == index) {
                return current.data;
            }

            current = current.next;
            counter++;
        }

        return null;
    }

    // Check if a value exists
    contains(data) {
        let current = this.head;

        while (current != null) {
            if (current.data == data) {
                return true;
            }

            current = current.next;
        }

        return false;
    }
}

module.exports = { LinkedList, Node };

