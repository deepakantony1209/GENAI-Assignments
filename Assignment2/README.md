# Assignment 2 - Sales and Discount System

## Overview

This assignment focuses on sales management, discount calculations, order processing, and user interaction through a menu-driven interface.

## Files

### 1. discountRules.py

Implements a discount calculation system based on order amounts.

- Calculates tiered discounts for different order values
- Applies tax to the discounted amount
- Outputs the final total amount to be paid

**Features:**

- Order amount input validation
- Tiered discount tiers:
  - 15% discount for orders ≥ $2000
  - 10% discount for orders $1500-$1999
  - 7% discount for orders $1000-$1499
  - No discount for orders < $1000
- Tax calculation (5%)
- Total amount display

### 2. dailySales.py

Manages daily sales data and calculations.

### 3. multipleOrderProcess.py

Processes multiple orders with batch operations.

### 4. userMenu.py

Provides a menu-driven interface for user interactions and order management.

## Usage

Run each script individually based on your needs:

```bash
python discountRules.py
python dailySales.py
python multipleOrderProcess.py
python userMenu.py
```

## Requirements

- Python 3.x
