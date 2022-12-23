while True:
    operation_selection = int(input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Reverse matrix
0. Exit
User : """))
    counter_of_matrices = 0


    def add_matrices():
        matrix_lines = int(input("Input the number of lines : "))
        matrix_columns = int(input("Input the number of columns : "))
        matrix_A = []
        matrix_B = []
        matrix_AB = []
        counter_lines = 0
        row_filling = None
        element_number_in_the_string = 0
        number_of_string = 0
        while counter_lines < matrix_lines:
            matrix_A.append([row_filling] * matrix_columns)
            matrix_B.append([row_filling] * matrix_columns)
            matrix_AB.append([row_filling] * matrix_columns)
            counter_lines += 1
        print(*matrix_A, sep="\n")
        while True:
            matrix_digit = int(input(f"Input value for matrix A :  "))
            matrix_A[number_of_string][element_number_in_the_string] = matrix_digit
            element_number_in_the_string += 1
            if element_number_in_the_string == matrix_columns:
                element_number_in_the_string = 0
                number_of_string += 1
            print(*matrix_A, sep="\n")
            if matrix_A[matrix_lines - 1][matrix_columns - 1] == matrix_digit:
                number_of_string = 0
                element_number_in_the_string = 0
                break
        while True:
            matrix_digit = int(input(f"Input value for matrix B : "))
            matrix_B[number_of_string][element_number_in_the_string] = matrix_digit
            element_number_in_the_string += 1
            if element_number_in_the_string == matrix_columns:
                element_number_in_the_string = 0
                number_of_string += 1
            print(*matrix_B, sep="\n")
            if matrix_B[matrix_lines - 1][matrix_columns - 1] == matrix_digit:
                number_of_string = 0
                element_number_in_the_string = 0
                break
        while True:
            matrix_AB[number_of_string][element_number_in_the_string] = \
                matrix_A[number_of_string][element_number_in_the_string] + \
                matrix_B[number_of_string][element_number_in_the_string]
            element_number_in_the_string += 1
            if element_number_in_the_string == matrix_columns:
                element_number_in_the_string = 0
                number_of_string += 1
            if not matrix_AB[matrix_lines - 1][matrix_columns - 1] == None:
                print("MatrixAB :", *matrix_AB, sep="\n")
                break


    def multiply_matrix_by_a_constant():
        matrix_lines = int(input("Input the number of lines : "))
        matrix_columns = int(input("Input the number of columns : "))
        const = int(input("Input the const : "))
        matrix_A = []
        result = []
        counter_lines = 0
        row_filling = None
        element_number_in_the_string = 0
        number_of_string = 0
        while counter_lines < matrix_lines:
            matrix_A.append([row_filling] * matrix_columns)
            result.append([row_filling] * matrix_columns)
            counter_lines += 1
        print(*matrix_A, sep="\n")
        while True:
            matrix_digit = int(input(f"Input value for matrix A :  "))
            matrix_A[number_of_string][element_number_in_the_string] = matrix_digit
            element_number_in_the_string += 1
            if element_number_in_the_string == matrix_columns:
                element_number_in_the_string = 0
                number_of_string += 1
            print(*matrix_A, sep="\n")
            if matrix_A[matrix_lines - 1][matrix_columns - 1] == matrix_digit:
                number_of_string = 0
                element_number_in_the_string = 0
                break
        while True:
            result[number_of_string][element_number_in_the_string] = \
                matrix_A[number_of_string][element_number_in_the_string] * const
            element_number_in_the_string += 1
            if element_number_in_the_string == matrix_columns:
                element_number_in_the_string = 0
                number_of_string += 1
            if not result[matrix_lines - 1][matrix_columns - 1] == None:
                print("ConstMatrix :", *result, sep="\n")
                break


    def multiply_matrices():
        matrixA_lines = int(input("Input the number of lines for A matrix : "))
        matrixA_columns = int(input("Input the number of columns for A matrix : "))
        matrixB_lines = int(input("Input the number of lines for B matrix : "))
        matrixB_columns = int(input("Input the number of columns for B matrix : "))
        matrixAB_lines = min(matrixA_lines, matrixB_lines)
        matrixAB_columns = min(matrixA_columns, matrixB_columns)
        if matrixA_lines == matrixB_columns or matrixA_columns == matrixB_lines:
            matrix_A = []
            matrix_B = []
            matrix_AB = []
            parts_of_matrix_AB = []
            counter_lines = 0
            row_filling = None
            element_number_in_the_string = 0
            number_of_string = 0
            element_of_column_matrixAB = 0
            counter_for_lines_matrixAB = 0
            while counter_lines < matrixA_lines:
                matrix_A.append([row_filling] * matrixA_columns)
                counter_lines += 1
            print(f"Matrix A : ", *matrix_A, sep="\n")
            counter_lines = 0
            while counter_lines < matrixB_lines:
                matrix_B.append([row_filling] * matrixB_columns)
                counter_lines += 1
            print(f"Matrix B  : ", *matrix_B, sep="\n")
            counter_lines = 0
            while counter_lines < matrixAB_lines:
                matrix_AB.append([row_filling] * matrixAB_columns)
                counter_lines += 1
            print(f"Matrix AB  : ", *matrix_AB, sep="\n")
            counter_lines = 0
            while counter_lines < matrixAB_lines * matrixAB_columns:
                parts_of_matrix_AB.append([0])
                counter_lines += 1
            while True:
                matrix_digit = int(input(f"Input value for matrix A :  "))
                matrix_A[number_of_string][element_number_in_the_string] = matrix_digit
                element_number_in_the_string += 1
                if element_number_in_the_string == matrixA_columns:
                    element_number_in_the_string = 0
                    number_of_string += 1
                print(*matrix_A, sep="\n")
                if matrix_A[matrixA_lines - 1][matrixA_columns - 1] == matrix_digit:
                    number_of_string = 0
                    element_number_in_the_string = 0
                    break
            while True:
                matrix_digit = int(input(f"Input value for matrix B : "))
                matrix_B[number_of_string][element_number_in_the_string] = matrix_digit
                element_number_in_the_string += 1
                if element_number_in_the_string == matrixB_columns:
                    element_number_in_the_string = 0
                    number_of_string += 1
                print(*matrix_B, sep="\n")
                if matrix_B[matrixB_lines - 1][matrixB_columns - 1] == matrix_digit:
                    number_of_string = 0
                    element_number_in_the_string = 0
                    break
            counter_for_parts = 0
            counter_for_columns_in_matrixA = 0
            counter_for_strings_in_matrixA = 0
            counter_for_columns_in_matrixB = 0
            counter_for_strings_in_matrixB = 0
            while not counter_for_strings_in_matrixA == matrixA_lines and counter_for_columns_in_matrixA < matrixA_columns:
                parts_of_matrix_AB[counter_for_parts][0] += \
                    matrix_A[counter_for_strings_in_matrixA][counter_for_columns_in_matrixA] * \
                    matrix_B[counter_for_strings_in_matrixB][counter_for_columns_in_matrixB]
                counter_for_columns_in_matrixA += 1
                counter_for_strings_in_matrixB += 1
                if counter_for_columns_in_matrixA == matrixA_columns:
                    counter_for_parts += 1
                    counter_for_columns_in_matrixA = 0
                    counter_for_strings_in_matrixB = 0
                    counter_for_columns_in_matrixB += 1
                if counter_for_columns_in_matrixB == matrixB_columns:
                    counter_for_columns_in_matrixB = 0
                    counter_for_strings_in_matrixA += 1
            counter_for_parts = 0
            while matrix_AB[-1][-1] == None:
                matrix_AB[counter_for_lines_matrixAB][element_of_column_matrixAB] = \
                    parts_of_matrix_AB[counter_for_parts][0]
                element_of_column_matrixAB += 1
                counter_for_parts += 1
                if element_of_column_matrixAB == matrixAB_columns:
                    element_of_column_matrixAB = 0
                    counter_for_lines_matrixAB += 1
            print(f"Matrix AB :", *matrix_AB, sep="\n")


        else:
            print("Error")


    def transpose_matrix():
        type_of_transpose_matrix = int(input("""Input the type of transpose_matrix:
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
User: """))
        matrix_lines = int(input("Input the number of lines : "))
        matrix_columns = int(input("Input the number of columns : "))
        matrix_A = []
        counter_lines = 0
        row_filling = None
        element_number_in_the_string = 0
        number_of_string = 0

        while counter_lines < matrix_lines:
            matrix_A.append([row_filling] * matrix_columns)
            counter_lines += 1
        print(*matrix_A, sep="\n")
        counter_lines = 0
        while True:
            matrix_digit = int(input(f"Input value for matrix A :  "))
            matrix_A[number_of_string][element_number_in_the_string] = matrix_digit
            element_number_in_the_string += 1
            if element_number_in_the_string == matrix_columns:
                element_number_in_the_string = 0
                number_of_string += 1
            print(*matrix_A, sep="\n")
            if matrix_A[matrix_lines - 1][matrix_columns - 1] == matrix_digit:
                number_of_string = 0
                element_number_in_the_string = 0
                break
        if type_of_transpose_matrix == 1:
            counter_for_columns_in_matrixA = 0
            counter_for_lines_in_matrixA = 0
            counter_for_columns_in_result = 0
            counter_for_lines_in_result = 0
            result_matrix_lines = matrix_columns
            result_matrix_columns = matrix_lines
            result = []
            while counter_lines < result_matrix_lines:
                result.append([row_filling] * result_matrix_columns)
                counter_lines += 1
            while result[-1][-1] == None:
                result[counter_for_lines_in_result][counter_for_columns_in_result] = \
                    matrix_A[counter_for_lines_in_matrixA][counter_for_columns_in_matrixA]
                counter_for_lines_in_matrixA += 1
                counter_for_columns_in_result += 1
                if counter_for_lines_in_matrixA == matrix_lines:
                    counter_for_lines_in_matrixA = 0
                    counter_for_columns_in_result = 0
                    counter_for_columns_in_matrixA += 1
                    counter_for_lines_in_result += 1
            print(f"Result matrix:", *result, sep="\n")
        elif type_of_transpose_matrix == 2:
            counter_for_columns_in_matrixA = 0
            counter_for_lines_in_matrixA = 0
            counter_for_columns_in_result = -1
            counter_for_lines_in_result = -1
            result = []
            result_matrix_lines = matrix_columns
            result_matrix_columns = matrix_lines
            while counter_lines < result_matrix_lines:
                result.append([row_filling] * result_matrix_columns)
                counter_lines += 1
            while result[0][0] is None:
                result[counter_for_lines_in_result][counter_for_columns_in_result] = \
                    matrix_A[counter_for_lines_in_matrixA][counter_for_columns_in_matrixA]
                counter_for_lines_in_matrixA += 1
                counter_for_columns_in_result -= 1
                if counter_for_lines_in_matrixA == matrix_lines:
                    counter_for_columns_in_matrixA += 1
                    counter_for_lines_in_result -= 1
                    counter_for_lines_in_matrixA = 0
                    counter_for_columns_in_result = -1
            print("Result matrix: ", *result, sep="\n")
        elif type_of_transpose_matrix == 3:
            counter_for_columns_in_matrixA = 0
            counter_for_lines_in_matrixA = 0
            counter_for_columns_in_result = -1
            counter_for_lines_in_result = 0
            result = []
            while counter_lines < matrix_lines:
                result.append([row_filling] * matrix_columns)
                counter_lines += 1
            while counter_for_lines_in_matrixA < matrix_lines:
                result[counter_for_lines_in_result][counter_for_columns_in_result] = \
                    matrix_A[counter_for_lines_in_matrixA][counter_for_columns_in_matrixA]
                counter_for_columns_in_result -= 1
                counter_for_columns_in_matrixA += 1
                if counter_for_columns_in_matrixA == matrix_columns:
                    counter_for_lines_in_matrixA += 1
                    counter_for_lines_in_result += 1
                    counter_for_columns_in_matrixA = 0
                    counter_for_columns_in_result = -1
            print("Result matrix: ", *result, sep="\n")
        elif type_of_transpose_matrix == 4:
            counter_for_columns_in_matrixA = 0
            counter_for_lines_in_matrixA = 0
            counter_for_columns_in_result = 0
            counter_for_lines_in_result = -1
            result = []
            while counter_lines < matrix_lines:
                result.append([row_filling] * matrix_columns)
                counter_lines += 1
            while counter_for_lines_in_matrixA < matrix_lines:
                result[counter_for_lines_in_result][counter_for_columns_in_result] = \
                    matrix_A[counter_for_lines_in_matrixA][counter_for_columns_in_matrixA]
                counter_for_columns_in_matrixA += 1
                counter_for_columns_in_result += 1
                if counter_for_columns_in_matrixA == matrix_columns:
                    counter_for_columns_in_matrixA = 0
                    counter_for_columns_in_result = 0
                    counter_for_lines_in_matrixA += 1
                    counter_for_lines_in_result -= 1
            print("Result matrix: ", *result, sep="\n")
        else:
            print("Not corrected value!")


    def calculate_a_determinant():
        matrix_lines = int(input("Input the number of lines : "))
        matrix_columns = int(input("Input the number of columns : "))
        det_A = []
        counter_lines = 0
        row_filling = None
        element_number_in_the_string = 0
        number_of_string = 0

        while counter_lines < matrix_lines:
            det_A.append([row_filling] * matrix_columns)
            counter_lines += 1
        print(*det_A, sep="\n")
        counter_lines = 0
        while True:
            matrix_digit = int(input(f"Input value for det A :  "))
            det_A[number_of_string][element_number_in_the_string] = matrix_digit
            element_number_in_the_string += 1
            if element_number_in_the_string == matrix_columns:
                element_number_in_the_string = 0
                number_of_string += 1
            print(*det_A, sep="\n")
            if det_A[matrix_lines - 1][matrix_columns - 1] == matrix_digit:
                number_of_string = 0
                element_number_in_the_string = 0
                break

        def determ_matrix(det_A, n):
            match n:
                case 1:
                    return det_A[0][0]
                case 2:
                    return det_A[0][0] * det_A[1][1] - det_A[1][0] * det_A[0][1]
                case n:
                    s = 0
                    for i in range(n):
                        mn = []
                        for k in range(n):
                            r = []
                            for j in range(n):
                                if k != 0 and j != i:
                                    r += [det_A[k][j]]
                            if r != []:
                                mn += [r]
                        s += det_A[0][i] * (determ_matrix(mn, n - 1) * (-1) ** i)
                    return s

        print(determ_matrix(det_A, matrix_lines))


    def determinant(matrix_A: list):
        if len(matrix_A) == len(matrix_A[0]) == 1:
            return matrix_A[0][0]
        height = len(matrix_A)
        determ = 0
        for i in range(height):
            minor_symbol = (-1) ** i
            determ += (determinant(minor(matrix_A, i, 0)) * minor_symbol * matrix_A[i][0])
        return determ


    def minor(matrix_A, i, j):
        height = len(matrix_A)
        minor = []
        for horizontal in range(height):
            minor_height = []
            if horizontal == i:
                continue
            for vertical in range(height):
                if vertical == j:
                    continue
                minor_height.append(matrix_A[horizontal][vertical])
            minor.append(minor_height)
        return minor


    def reverse_matrix():
        matrix_lines = int(input("Input the number of lines : "))
        matrix_columns = int(input("Input the number of columns : "))
        matrix_A = []
        counter_lines = 0
        row_filling = None
        element_number_in_the_string = 0
        number_of_string = 0

        while counter_lines < matrix_lines:
            matrix_A.append([row_filling] * matrix_columns)
            counter_lines += 1
        print(*matrix_A, sep="\n")
        counter_lines = 0
        while True:
            matrix_digit = int(input(f"Input value for matrix A :  "))
            matrix_A[number_of_string][element_number_in_the_string] = matrix_digit
            element_number_in_the_string += 1
            if element_number_in_the_string == matrix_columns:
                element_number_in_the_string = 0
                number_of_string += 1
            print(*matrix_A, sep="\n")
            if matrix_A[matrix_lines - 1][matrix_columns - 1] == matrix_digit:
                number_of_string = 0
                element_number_in_the_string = 0
                break

        height = len(matrix_A)
        inversed_matrix = []
        for i in range(height):
            matrix_height = []
            for j in range(height):
                minor_symbol = (-1) ** (i + j)
                matrix_height.append(determinant(minor(matrix_A, i, j)) * minor_symbol)

            inversed_matrix.append(matrix_height)
        print("Inversed matrix:")
        print(*inversed_matrix, sep="\n")


    if operation_selection == 1:
        add_matrices()
    elif operation_selection == 2:
        multiply_matrix_by_a_constant()
    elif operation_selection == 3:
        print(
            "        WARNING\nThe number of rows of one matrix must match the number of columns of the second matrix")
        multiply_matrices()
    elif operation_selection == 4:
        transpose_matrix()
    elif operation_selection == 5:
        print("WARNING\nThe number of rows of matrix must match the number of columns ")
        calculate_a_determinant()
    elif operation_selection == 6:
        reverse_matrix()
    elif operation_selection == 0:
        exit()
    else:
        print("Not correct value!")
