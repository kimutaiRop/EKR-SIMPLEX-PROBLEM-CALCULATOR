import sys
import numpy as np
from fractions import Fraction

try:
    import pandas as pd
    pandas_av = True
except ImportError:
    pandas_av = False
    pass

product_names = []
col_values = []
z_equation = []
final_rows = []
solutions = []
x = 'X'
z2_equation = []
removable_vars = []
no_solution = """
        ---unboundedness ----
Your problem might not be having solution due to wrong 
formulation of constrains,

This mostly occurs when you leave out some relevant constrains 
please check again the formulation of constrains
            """


def main():
    global decimals
    global const_num, prod_nums
    print("""
    EKR-SIMPLEX CALCULATOR
    
what type of problem do you want to solve?	
    1 :maximization (<=).
    2 :minimization (>=).
        
    0 :For Help.
    """)
    try:
        prob_type = int(input("enter the number problem type: >"))
    except ValueError:
        print("please enter a number from choices above")
        prob_type = int(input("enter the number problem type: >"))
    if prob_type != 2 and prob_type != 1 and prob_type != 0:
        sys.exit("you enter a wrong problem choice ->" + str(prob_type))
    if prob_type == 0:
        print(r"""
        --HELP:
        USING SIMPLEX CALCULATOR
        
        ----- requirements -----
        
        1 -> python - install python (https://www.python.org)
        2 -> pip    - install pip (google for your Operating System)
        3 -> numpy  - pip install numpy  - required!!
        4 -> pandas - pip install pandas - optional - makes the tableus more beautiful and orderly
        
        ----- choices -----
        
        1 -> Simplex maximization problems like maximization of profits
        2 -> Simplex minimization problem like minimization of expenditure in company
        0 -> Help on using the calculator
        
        ----- best data -----
        
        please rename your products to X1, X2, X3...Xn
        for easy feeding of data
        
        n - being the number of products you have
        
        example: computers - X1
                 printers  - X2

        you can use: - whole numbers
                     - decimal numbers
                     - fractions
                Entering the value you are prompted to. the decimal are not 
                rounded off on entering. this ensures high accuracy.
                for recurring and long fractions, ie. (1/3). the decimal places are ronded of 
                to default of python
         
        you are advised to use values less than 10000000
        you can standardize the data by dividing it to small values
        and re-converting after getting solution
         
        big values are used for slack in this program.
        so using big values may lead to confusion of data with the
        slack variables in some cases
          
        
        ----- assumptions -----
        
        I assume that you know how to read the simplex table.
        I also assume that you know how to interpret the data in the table and So 
        I did not interpret the data 
        
        This program is to be used by statisticians and also those with
        an idea about the simplex problems
        
        This programs though need no much knowledge on mathematics/statistics
        
        ----- mixed simplex problem -----
          
        I have not made a choice for mixed simplex problem and so for now 
        the program may not provide a solution for such problems
         
        ----- disclaimer -----
        
        Only the console  option of this program is available yet but the GUI might be available
        at some point and when available, I will update on how to use the GUI.
          
        The program has been tested with several examples but maybe all the exception 
        may not have been countered fully. using this program will be an alternative
        you chose and so we I am not expecting a complain in failure to meet your expectation as indicated in the LICENCE.
          
        #You can suggest additions or even send me bugs in the program in the email below.#
          
        kimrop20@gmail.com
        
        
           
        ----- licence -----
        
        This program is to be used freely. You can also re-edit or modify or even add to
        this program.
        you can also share but you should not change the developer ownership.
        
        I will appreciate credit given to me
        
        ----- developer -----
          
        developed by [ELPHAS KIMUTAI ROP] .
        Graduate Bsc. Statistics and programming.
        Machakos University, Kenya.
        Email   : kimrop20@gmail.com
        Website : https://bestcoders.net
         
        
         
        """)
        sys.exit()
    print('\n##########################################')
    global const_names
    const_num = int(input("how many products do you have: >"))
    prod_nums = int(input("how many constrains do you have: >"))
    const_names = [x + str(i) for i in range(1, const_num + 1)]
    for i in range(1, prod_nums + 1):
        prod_val = input("enter constrain {} name: >".format(i))
        product_names.append(prod_val)
    print("__________________________________________________")
    if prob_type == 1:
        for i in const_names:
            try:
                val = float(Fraction(input("enter the value of %s in Z equation: >" % i)))
            except ValueError:
                print("please enter a number")
                val = float(Fraction(input("enter the value of %s in Z equation: >" % i)))
            z_equation.append(0 - val)
        z_equation.append(0)

        while len(z_equation) <= (const_num + prod_nums):
            z_equation.append(0)
        print("__________________________________________________")
        for prod in product_names:
            for const in const_names:
                try:
                    val = float(Fraction(input("enter the value of %s in %s: >" % (const, prod))))
                except ValueError:
                    print("please ensure you enter a number")
                    val = float(Fraction(input("enter the value of %s in %s: >" % (const, prod))))
                col_values.append(val)
            equate_prod = float(Fraction(input('equate %s to: >' % prod)))
            col_values.append(equate_prod)

        final_cols = stdz_rows(col_values)
        i = len(const_names) + 1
        while len(const_names) < len(final_cols[0]) - 1:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        const_names.append('Solution')
        final_cols.append(z_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("_____________________________________________")
        decimals = int(input('Number of roundoff decimals : '))
        print('\n##########################################')
        maximization(final_cols, final_rows)

    elif prob_type == 2:
        for i in const_names:
            try:
                val = float(Fraction(input("enter the value of %s in Z equation: >" % i)))
            except ValueError:
                print("please enter a number")
                val = float(Fraction(input("enter the value of %s in Z equation: >" % i)))
            z_equation.append(val)
        z_equation.append(0)

        while len(z_equation) <= (const_num + prod_nums):
            z_equation.append(0)
        print("__________________________________________________")
        for prod in product_names:
            for const in const_names:
                try:
                    val = float(Fraction(input("enter the value of %s in %s: >" % (const, prod))))
                except ValueError:
                    print("please ensure you enter a number")
                    val = float(Fraction(input("enter the value of %s in %s: >" % (const, prod))))
                col_values.append(val)
            equate_prod = float(Fraction(input('equate %s to: >' % prod)))
            col_values.append(equate_prod)

        final_cols = stdz_rows2(col_values)
        i = len(const_names) + 1
        while len(const_names) < prod_nums + const_num:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        solutions[:] = []
        add_from = len(const_names) + 1
        while len(const_names) < len(final_cols[0][:-1]):
            removable_vars.append('X' + str(add_from))
            const_names.append('X' + str(add_from))
            add_from += 1
        removable_vars.append(' Z')
        removable_vars.append('Z1')
        const_names.append('Solution')
        for ems in removable_vars:
            solutions.append(ems)
        while len(z_equation) < len(final_cols[0]):
            z_equation.append(0)
        final_cols.append(z_equation)
        final_cols.append(z2_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("________________________________")
        decimals = int(input('Number of roundoff decimals : '))
        print('\n##########################################')
        minimization(final_cols, final_rows)

    else:
        sys.exit("you enter a wrong problem choice ->" + str(prob_type))


def maximization(final_cols, final_rows):
    row_app = []
    last_col = final_cols[-1]
    min_last_row = min(last_col)
    min_manager = 1
    print(" 1 TABLEAU")
    try:
        final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        print(final_pd)
    except:
        print('  ', const_names)
        i = 0
        for cols in final_cols:
            print(solutions[i], cols)
            i += 1
    count = 2
    pivot_element = 2
    while min_last_row < 0 < pivot_element != 1 and min_manager == 1 and count < 6:
        print("*********************************************************")
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col

            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows

        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('pivot element: %s' % pivot_element)
        print('pivot column: ', pivot_row)
        print('pivot row: ', pivot_col)
        print("\n")
        solutions[index_pivot_col] = const_names[index_pivot_row]

        print(" %d TABLEAU" % count)
        try:
            final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
            print(final_pd)
        except:
            print("%d TABLEAU" % count)
            print('  ', const_names)
            i = 0
            for cols in final_cols:
                print(solutions[i], cols)
                i += 1
        count += 1
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        if pivot_element < 0:
            print(no_solution)
    if not pandas_av:
        print("""
        Please install pandas to make your tables look good
        install using command $pip install pandas 
        """)


def minimization(final_cols, final_rows):
    row_app = []
    last_col = final_cols[-1]
    min_last_row = min(last_col)
    min_manager = 1
    print("1 TABLEAU")
    try:
        fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        print(fibal_pd)
    except:
        print('  ', const_names)
        i = 0
        for cols in final_cols:
            print(solutions[i], cols)
            i += 1
    count = 2
    pivot_element = 2
    while min_last_row < 0 < pivot_element and min_manager == 1:
        print("*********************************************************")
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col[:-1])
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('pivot element: %s' % pivot_element)
        print('pivot column: ', pivot_row)
        print('pivot row: ', pivot_col)
        print("\n")
        removable = solutions[index_pivot_col]
        solutions[index_pivot_col] = const_names[index_pivot_row]
        if removable in removable_vars:
            idex_remove = const_names.index(removable)
            for colms in final_cols:
                colms.remove(colms[idex_remove])
            const_names.remove(removable)
        print("%d TABLEAU" % count)
        try:
            fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
            print(fibal_pd)
        except:
            print('  ', const_names)
            i = 0
            for cols in final_cols:
                print(solutions[i], cols)
                i += 1
        count += 1
        final_rows[:] = []
        new_final_rows = np.array(final_cols).T.tolist()
        for _list in new_final_rows:
            final_rows.append(_list)

        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col[:-1])
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        if pivot_element < 0:
            print(no_solution)

    if not pandas_av:
        print("""
        Please install pandas to make your tables look good
        install using command $pip install pandas 
        """)


def stdz_rows2(column_values):
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]
    sum_z = (0 - np.array(final_cols).sum(axis=0)).tolist()
    for _list in sum_z:
        z2_equation.append(_list)

    for cols in final_cols:
        while len(cols) < (const_num + (2 * prod_nums) - 1):
            cols.insert(-1, 0)

    i = const_num
    for sub_col in final_cols:
        sub_col.insert(i, -1)
        z2_equation.insert(-1, 1)
        i += 1

    for sub_col in final_cols:
        sub_col.insert(i, 1)
        i += 1

    while len(z2_equation) < len(final_cols[0]):
        z2_equation.insert(-1, 0)

    return final_cols


def stdz_rows(column_values):
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]
    for cols in final_cols:
        while len(cols) < (const_num + prod_nums):
            cols.insert(-1, 0)

    i = const_num
    for sub_col in final_cols:
        sub_col.insert(i, 1)
        i += 1

    return final_cols


if __name__ == "__main__":
    main()

# I use python list and arrays(numpy) in most of this program
# it became simple coz python has a strong power in list and array manipulation and solution
