#!/usr/bin/env python3
"""
PAGINATION SYSTEM
Topics: Classes, Method Chaining, List Slicing, Error Handling
"""

import math


class Pagination:
    """
    A pagination class that breaks large lists into manageable pages.
    Supports method chaining for fluent navigation.
    """
    
    def __init__(self, items=None, page_size=10):
        """
        Initialize pagination with items and page size.
        
        Args:
            items: List of items to paginate (default: empty list)
            page_size: Number of items per page (default: 10)
        """
        # Handle None items
        if items is None:
            self.items = []
        else:
            self.items = items
        
        self.page_size = page_size
        self.current_idx = 0  # 0-based internal index
        
        # Calculate total pages
        if self.items:
            self.total_pages = math.ceil(len(self.items) / self.page_size)
        else:
            self.total_pages = 0
    
    def get_visible_items(self):
        """
        Return items visible on current page.
        Note: This returns the list, not self (breaks chain)
        """
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    
    def go_to_page(self, page_num):
        """
        Navigate to specific page (1-based user input).
        Raises ValueError if page is out of range.
        
        Args:
            page_num: Page number to navigate to (1-based)
        """
        # Convert to 0-based index
        target_idx = page_num - 1
        
        # Validate range
        if target_idx < 0 or target_idx >= self.total_pages:
            raise ValueError(f"Invalid page number {page_num}. "
                           f"Valid range: 1 to {self.total_pages}")
        
        self.current_idx = target_idx
        return self  # Enable method chaining
    
    def first_page(self):
        """Navigate to first page."""
        self.current_idx = 0
        return self  # Enable method chaining
    
    def last_page(self):
        """Navigate to last page."""
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self  # Enable method chaining
    
    def next_page(self):
        """Move one page forward if not on last page."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self  # Enable method chaining
    
    def previous_page(self):
        """Move one page backward if not on first page."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self  # Enable method chaining
    
    def __str__(self):
        """
        Magic method: Display items on current page, each on new line.
        """
        visible = self.get_visible_items()
        if not visible:
            return "(No items on this page)"
        return "\n".join(str(item) for item in visible)
    
    def __repr__(self):
        """Official string representation."""
        return (f"Pagination(items={len(self.items)}, "
                f"page_size={self.page_size}, "
                f"current_page={self.current_idx + 1}, "
                f"total_pages={self.total_pages})")


# ============================================================
# TESTING THE PAGINATION SYSTEM
# ============================================================

def main():
    print("=" * 60)
    print("📄 PAGINATION SYSTEM TESTS")
    print("=" * 60)
    
    # Setup test data
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    print(f"\nTest data: {alphabetList}")
    print(f"Total items: {len(alphabetList)}")
    
    # Create pagination with page size 4
    p = Pagination(alphabetList, 4)
    print(f"\nCreated pagination: {p}")
    
    # Test 1: Initial page
    print("\n" + "-" * 40)
    print("Test 1: Initial page (page 1)")
    print(f"Visible items: {p.get_visible_items()}")
    # Expected: ['a', 'b', 'c', 'd']
    
    # Test 2: Next page
    print("\n" + "-" * 40)
    print("Test 2: After next_page()")
    p.next_page()
    print(f"Visible items: {p.get_visible_items()}")
    # Expected: ['e', 'f', 'g', 'h']
    
    # Test 3: Last page
    print("\n" + "-" * 40)
    print("Test 3: Jump to last page")
    p.last_page()
    print(f"Visible items: {p.get_visible_items()}")
    # Expected: ['y', 'z']
    
    # Test 4: Go to specific page
    print("\n" + "-" * 40)
    print("Test 4: Go to page 3")
    p.go_to_page(3)
    print(f"Visible items: {p.get_visible_items()}")
    print(f"Current page index + 1: {p.current_idx + 1}")
    
    # Test 5: Error handling - invalid page
    print("\n" + "-" * 40)
    print("Test 5: Invalid page (should raise ValueError)")
    try:
        p.go_to_page(10)
        print("ERROR: Should have raised ValueError!")
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")
    
    # Test 6: Error handling - page 0
    print("\n" + "-" * 40)
    print("Test 6: Page 0 (should raise ValueError)")
    try:
        p.go_to_page(0)
        print("ERROR: Should have raised ValueError!")
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")
    
    # Test 7: Method chaining (BONUS)
    print("\n" + "-" * 40)
    print("Test 7: Method Chaining")
    print("p.first_page().next_page().next_page().next_page()")
    
    # Reset and chain
    p.first_page()
    result = p.next_page().next_page().next_page().get_visible_items()
    print(f"Result: {result}")
    # Expected: ['m', 'n', 'o', 'p'] (pages: 2→3→4, so index 3 = page 4)
    
    # Alternative chain starting from beginning
    print("\nAlternative chain from first page:")
    p.first_page()
    # Page 1 (idx 0): a,b,c,d
    # Page 2 (idx 1): e,f,g,h  
    # Page 3 (idx 2): i,j,k,l
    # Page 4 (idx 3): m,n,o,p
    chained_result = p.first_page().next_page().next_page().next_page().get_visible_items()
    print(f"first_page().next_page().next_page().next_page(): {chained_result}")
    
    # Test 8: __str__ method
    print("\n" + "-" * 40)
    print("Test 8: __str__ method (print pagination object)")
    p.first_page()
    print("Current page contents:")
    print(str(p))
    
    # Test 9: Previous page
    print("\n" + "-" * 40)
    print("Test 9: Previous page navigation")
    p.go_to_page(3)
    print(f"On page 3: {p.get_visible_items()}")
    p.previous_page()
    print(f"After previous_page(): {p.get_visible_items()}")
    
    # Test 10: Empty list
    print("\n" + "-" * 40)
    print("Test 10: Empty list handling")
    empty_p = Pagination(None, 5)
    print(f"Empty pagination: {empty_p}")
    print(f"Visible items: {empty_p.get_visible_items()}")
    print(str(empty_p))
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED! ✅")
    print("=" * 60)


if __name__ == "__main__":
    main()