# c2CFG

*Need to update the python tool to work from any directory.*

## Overview
**c2CFG** is an innovative tool designed to assist programmers in understanding the control flow structure of C code. Named after its primary function, which is to convert C code into its corresponding Control Flow Graph (CFG).

## How to use:

> It is preferred that you keep this tool on the parent directory of the C files. For example, if .c files exist in `/home/user/Desktop/Files/C-files` move and run the tool in `/home/user/Desktop/Files`

		git clone https://github.com/kaushikakshat/c2CFG.git
		cd c2CFG/
		cp c2CFG.sh /<parent directory of .c files>
		cp c2CFG.py /<parent directory of .c files>
### .sh Script:
	    chmod +x c2CFG.sh
	    ./c2CFG.sh /<directory of C files>
### Python Script:
		python3 c2CFG.py /<directory of C files>

## Features:
1.  **Conversion to CFG:** c2CFG takes C code as input and generates its CFG representation. This representation illustrates how control flows through the program, making it easier to comprehend complex logic and identify potential issues.
    
2.  **Format Flexibility:** Users have the option to generate CFGs in either PNG or PDF format, providing versatility in how they choose to view and share the graphical representation.
    
3.  **Customization:** The tool offers various customization options to tailor the appearance of the generated CFGs according to individual preferences. Users can adjust node shapes, colors, and other visual elements to enhance clarity.
    
4.  **Integration:** c2CFG seamlessly integrates into existing development workflows, allowing programmers to incorporate CFG generation directly into their coding and debugging processes. Integration with IDEs or build systems can further streamline this process.
    
5.  **Accessibility:** With an intuitive interface and straightforward operation, c2CFG is accessible to both novice and experienced programmers alike. Its simplicity ensures that users can quickly grasp the functionality and start utilizing it effectively.

## Use Cases:

1.  **Code Understanding:** c2CFG aids in comprehending the structure and behavior of C code by providing a visual representation of its control flow. This is particularly useful when analyzing unfamiliar or complex codebases.
    
2.  **Debugging Assistance:** Visualizing the control flow of a program can assist developers in identifying logical errors, loops, and potential points of failure more efficiently. By pinpointing problematic areas visually, debugging becomes more systematic and effective.
    
3.  **Documentation:** Generated CFGs can serve as documentation artifacts, helping in illustrating the high-level logic and design of a program. Including CFGs in project documentation enhances readability and facilitates communication among team members.

## Conclusion: 
c2CFG simplifies the process of understanding and analyzing C code by providing clear and intuitive visualizations of its control flow. With its versatile features, seamless integration, and broad applicability, c2CFG empowers developers to navigate codebases effectively, debug with precision, and communicate concepts efficiently. Whether used for personal projects, professional development, or educational purposes, c2CFG proves to be an indispensable asset in the toolkit of any C programmer.
