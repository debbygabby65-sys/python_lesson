def sales_perfomance_analyzer():
    count = 0
    sales = {
        "debby": 1500,
        "gabby": 3000,
        "mary": 400000
    }
            
    total = sum(sales.values())
    print("Total:", total)

    average = total / len(sales.values())
    print("Average:", average)

    for name, price in sales.items():
     
        if price > average:
            count += 1
        else:
            count -= 1
   
    highest_sale = max(sales.values())
    print("Highest sales:", highest_sale)

    lowest_sale = min(sales.values())
    print("Lowest sales:", lowest_sale)

    print("count", count)

sales_perfomance_analyzer()

