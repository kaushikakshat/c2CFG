import os
import argparse

# Commands from: https://wisesciencewise.wordpress.com/2022/10/03/steps-to-generate-llvm-call-flow-graphcfg/

def commands_2(direc):
    """ This is where the magic happens of converting to PDF... """
    
    location1 = os.path.join(f"{direc}/../llvm-ir")
    os.mkdir(location1)

    location2 = os.path.join(f"{direc}/../pdf")
    os.mkdir(location2)

    # Command - 1
    for file in os.listdir(direc):
        if file.endswith(".c"):
            try:
                print("Converting C file to LLVM IR...")
                os.system(f"clang -S -emit-llvm {direc}/{file} -o {direc}/../llvm-ir/{file}.ll -w")
            except:
                print("Error occured while running clang!")
    
        # Command - 2
        os.system(f"opt -dot-cfg -disable-output {direc}/../llvm-ir/{file}.ll")
        
        # Command - 3
        os.system(f"dot -Tpdf -o {direc}/../pdf/{file[:-2]}.pdf {direc}/../.main.dot")

        os.system("rm .*.dot")


def commands(direc):
    """ This is where the magic happens of converting to PNG... """
    
    location1 = os.path.join(f"{direc}/../llvm-ir")
    os.mkdir(location1)

    location2 = os.path.join(f"{direc}/../png")
    os.mkdir(location2)

    # Command - 1
    for file in os.listdir(direc):
        if file.endswith(".c"):
            try:
                print("Converting C file to LLVM IR...")
                os.system(f"clang -S -emit-llvm {direc}/{file} -o {direc}/../llvm-ir/{file}.ll -w")
            except:
                print("Error occured while running clang!")
    
        # Command - 2
        os.system(f"opt -dot-cfg -disable-output {direc}/../llvm-ir/{file}.ll")
        
        # Command - 3
        os.system(f"dot -Tpng -o {direc}/../png/{file[:-2]}.png {direc}/../.main.dot")

        os.system("rm .*.dot")


def check_c_file_exists(abc):
    """ This function checks if C file/s exist in the directory. """

    print("Searching for C files...")

    # Variables
    count = 0
    arr = os.listdir(abc)

    # Logic
    for file in arr:
        if file.endswith(".c"):
            count += 1
        # print(file)
    if count == 0:
        print("No C file/s found!")
    elif count >= 1:
        print("File/s found!")
        format = int(input("Output options: \n 1. PNG \n 2. PDF \n Enter the choice index number: "))
        if format == 1:
            commands(abc)
        elif format == 2:
            commands_2(abc)
        else:
            print("Wrong command chosen!")
            return


def check(directory):
    """This function check if the path is vaild."""

    print("Checking if path is valid...")

    try:
        check_c_file_exists(directory)
        return
    except:
        print("Directory path invalid")


if __name__ == '__main__':

    msg = "Tool to convert all C files in a directory to CFG/s"

    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('input', type=str, help='path of input directory')
    args = parser.parse_args()

    print(f"Directory mentioned: {args.input}")
    check(args.input)
