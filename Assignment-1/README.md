# Python Data Structures - Assignments

This repository contains Python assignments demonstrating fundamental data structures: Lists, Tuples, Sets, and Dictionaries.

## Project Structure

### 1. **productCollections.py**

- **Purpose**: Store product data using basic data structures
- **Contents**:
  - `products` (List): List of car product names
  - `sample_product` (Tuple): Sample product with name, price, and type
- **Key Concepts**: Lists and Tuples

### 2. **categories.py**

- **Purpose**: Work with sets to manage product categories
- **Contents**:
  - `categories` (List): Parallel list of product categories
  - `categories_set` (Set): Unique product categories
- **Operations**:
  - Creating sets from lists
  - Adding new items to sets
  - Demonstrating duplicate handling
  - Checking membership with `in` operator
  - Finding unique count
- **Key Concepts**: Sets, membership testing, uniqueness

### 3. **productPricing.py**

- **Purpose**: Store and manage product prices using dictionaries
- **Contents**:
  - `prices` (List): Hardcoded prices for each product
  - `product_pricing` (Dictionary): Maps product names to prices
- **Operations**:
  - Creating dictionaries using `zip()`
  - Adding new key-value pairs
  - Removing items with error handling using try-except
  - Accessing dictionary values
- **Key Concepts**: Dictionaries, error handling, `zip()` function

### 4. **combinedOperations.py**

- **Purpose**: Combine multiple data structures for complex operations
- **Contents**:
  - `combined_operations` (List of Lists): Combines products, prices, and categories
  - `category_to_products` (Dictionary): Maps categories to lists of products
  - `product_to_categories` (Dictionary): Maps products to their categories
- **Operations**:
  - Creating combined data structures using list comprehensions
  - Building reverse mappings
  - Finding products with maximum categories
  - Analyzing category distribution
- **Key Concepts**: List comprehensions, nested data structures, data analysis

## Key Data Structures Used

| Structure      | Purpose                       | Example                                           |
| -------------- | ----------------------------- | ------------------------------------------------- |
| **List**       | Ordered, mutable collection   | `products = ["Swift", "Baleno", ...]`             |
| **Tuple**      | Ordered, immutable collection | `sample_product = ("Swift", 559000, "Hatchback")` |
| **Set**        | Unordered, unique items       | `categories_set = {"Maruti Suzuki", "Tata", ...}` |
| **Dictionary** | Key-value pairs               | `product_pricing = {"Swift": 559000, ...}`        |

## Key Functions & Methods

- `zip()` - Combines multiple iterables
- `enumerate()` - Gets index and value from iterable
- `set()` - Converts list to set (removes duplicates)
- `dict()` - Converts list of tuples to dictionary
- `.add()` - Adds item to set
- `.pop()` - Removes item from dictionary
- `in` operator - Checks membership in collections
- List comprehensions - Creates new lists with conditions

## Running the Scripts

```bash
# Activate virtual environment
venv\Scripts\activate

# Run individual scripts
python productCollections.py
python categories.py
python productPricing.py
python combinedOperations.py
```

## Sample Data

**Products:** Swift, Baleno, Tata Punch, Hyundai i20, Renault Kwid, XUV 3XO

**Categories:** Maruti Suzuki, Tata, Hyundai, Renault, Mahindra

**Price Range:** ₹379,000 - ₹859,000
