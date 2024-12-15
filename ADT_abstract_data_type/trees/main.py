from avl_tree import AVLTree
if __name__ == "__main__":
    # Create an instance of AVLTree
    avl = AVLTree()

    # Insert elements into the AVL tree
    elements_to_insert = [30, 20, 40, 10, 25, 35, 50]
    for elem in elements_to_insert:
        avl.add(elem)
        print(f"Inserted {elem}:")
        avl.print_tree()
        print("-" * 30)

    # Display traversals
    print("In-order Traversal:", avl.inorder_traversal())
    print("Pre-order Traversal:", avl.preorder_traversal())
    print("Post-order Traversal:", avl.postorder_traversal())

    # Search for elements
    search_keys = [25, 60]
    for key in search_keys:
        found = key in avl
        print(f"Search for {key}: {'Found' if found else 'Not Found'}")

    # Delete elements from the AVL tree
    elements_to_delete = [20, 30]
    for elem in elements_to_delete:
        avl.delete(elem)
        print(f"Deleted {elem}:")
        avl.print_tree()
        print("-" * 30)

    # Final traversals and checks
    print("Final In-order Traversal:", avl.inorder_traversal())
    print("Is the tree balanced?", avl.is_balanced())
    print(f"Tree Size: {len(avl)}")
