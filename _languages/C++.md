---
layout: language
language: c++
title: C++
---

<b><u>Overview </u></b>

C++ (pronounced "C-Plus-Plus") originally named "C with Classes" was developed by [Bjarne Stroustrup][stroutstrup_website_link], who aimed to add object-orientated programming  to C. It was designed for the use in system programming, where efficiency, performance and flexibility were the priority, thus providing many tools for low-level memory manipulation. Yet still supporting procedural and functional paradigms.

As of today, C++ is still one of the most popular [programming languages][popular_languages]. Mainly because nothing that handles complexity can [run as fast as C++][cpp_performace], and so it is [mainly used][cpp_applications] in development of games, device drivers, kernels, etc. where applications require direct communication with the hardware.

Perfect [quote][cpp_problems] to describe learning C++: "Java and C# teach you to swim in a kiddie pool with water wings, while C++ boots you naked off a cliff overlooking the breakers." C++ could be quite hard to learn, and some of its highlight features such as [templates][cpp_templates] have complex syntax, and require deep understanding to ensure their effective use. Although the main problem of the language, is not its complexity, but the subtlety to get it right. [There are cases where compiler accepts your code][cpp_problems], but language standard does not specify any behaviour, meaning anything could happen, even the code seems to be working fine; other languages would try to catch these kind of errors during compilation.  As well as many non standard libraries have very intricate interaction with each other, which at times can cause problems.

Some argue that C++ gives way too much control, for example nothing would stop a programmer from overloading "+" operator to mean subtraction or division or pretty much anything his/her heart desires it to be. So the only real reason to not like C++ is if you despise having near-absolute freedom when programming.

On the bright side, there are many different tutorials available [online][cpp_tutorial], ranging from basics, to the most advanced features of the language.

<b><u>Code!</u></b>

It should be said, as C is a [subset][cpp_c_compatibility] of C++, majority of basic programs that work in C will also work in C++, with little or no changes.


It is also very important to mention, that main file (file which contains main function) should be saved as "main.cpp".

Hello World:

{% highlight cpp %}

	#include <iostream>

    using namespace std;

    int main()
    {
        cout << "Hello World!" << endl;

        return 0;
    }

{% endhighlight cpp %}

Calculate [Mandelbrot points][mandelbrot_points], and export them to .csv file.

{% highlight cpp %}

    #include <iostream>
    #include <fstream>
    #include <string>
    #include <complex>
    #include <time.h>

    using namespace std;

    // Define Mandelbrot class
    class Mandelbrot
    {
        protected:
            // Define some variables
            complex<double> c;
            unsigned int numberofitterations;
        public:
            Mandelbrot(complex<double> C, int Numberofitterations) :
            c(C), numberofitterations(Numberofitterations)

            { /*Constructor*/}

            int escapedAt;
            int escapeVal()
            {
                return escapedAt;
            }
            bool check()
            {
                complex<double> ztmp;
                // Start loop, to check if point is mandelbrot
                for( int i = 0; i <= numberofitterations; i++)
                {
                    ztmp = ( ztmp * ztmp) + c;
                    if( abs(ztmp) > 2 )
                    {
                        escapedAt = i;
                        return false;
                    }
                }
                return true;
            }
    };

    int main()
    {
        double stepSize;
        int numberOfItterations;

        cout << "Please chose step size (0.001 is enough for 4k!): "; cin >> stepSize;  // Input of step size
        cout << "Please enter number of itterations (80 is plenty for first image!): "; cin >> numberOfItterations;  // Input number of itterations

        clock_t tStart = clock();  // Start timer

        cout << "Calculating. And writing to file." << endl;

        ofstream myFile("output.csv");  // Attempt to edit "output.csv" file
        if(myFile.is_open())
        {
            // Y
            for(double i= -2; i <= 2; i += stepSize)
            {
                // X
                for(double j = -2; j <= 2; j += stepSize)
                {
                    complex<double> a (j, i);

                    Mandelbrot m(a, numberOfItterations);  // Create a new instance of mandelbrot class
                    if(m.check())  // If point is mandelbrot
                    {
                        if((j != 2) && ( j + stepSize <= 2))  // If not first entry in the row
                        {
                            myFile << numberOfItterations << ",";  // Put number of iterations as an escape value
                        }
                        else myFile << numberOfItterations;  // If first entry in the row
                    }
                    else  // Else if point isn't mandelbrot
                    {
                        if((j != 2) && ( j + stepSize <= 2))
                            myFile << m.escapeVal() << ",";  // If not first entry in row, then place escape value
                        else myFile << m.escapeVal();
                    }

                }
                if((i != 2) && ( i + stepSize <= 2))
                    myFile << endl;  // Start the next line if not first entry in row
            }
        } else cout << "Can't open .csv file";  // If cannot open "output.csv" file

        printf("Time taken: %.2fs\n", ((double)clock() - tStart) / CLOCKS_PER_SEC);  // Display time taken to calculate the points

        cin.ignore();  // Wait for Enter key to be pressed

        return 0;
    }

{% endhighlight cpp %}


<b><u>Basic syntax</u></b>

There are many good [tutorials][cpp_tutorial] out there. I will just try to outline the fundamental syntax used in C++.

{% highlight cpp %}

    #include <iostream>
    #include <string>

    using namespace std;

    int main()
    {
        // This is a single line comment

        /*
        This is

        a

        multiline comment

        */


        // Declaring variables
        int age = 19;
        float favouriteNumber = 2.718;
        string name = "Seva";

        cout << "Hello! My name is " << name <<
             " , I am " << age << " years old." <<
             " My favourite number is " << favouriteNumber << endl;  // All one output instruction

        cin.ignore();  // Wait for Enter key to be pressed

        return 0;
    }

{% endhighlight cpp %}

The output of the code above will be:

"Hello my name is Seva, I'm 19 years old. My favourite number is 2.718".

First things first, C++ is a case sensitive language, which means `myNameIs` and `mynameis` are different!

Lines `#include <iostream>` and `#include <string>` are called headers, they tell compiler that we will use [methods][methods_wiki] from iostream and string [libraries][libraries_wiki].

Next line `using namespace std;` tells compiler to use std namespace. Essentially, if we didn't have this line, everytime we had to use method from either iostream or string library we would have to say `std::string name = "Seva";` and `std::cout << "Hello! My name is " << ... << std::endl;` I think you get the idea.

`int main()` now is this is the most important function in your whole program. This is where the execution of your program will begin.

Indentation is not required, but it is recommended for readability.

`{` In C++ curly brackets { } are equivalent to indentation in Python and "begin end" in pascal. They indicate which part of code is related to which function.

`// This is a single line comment` self explanatory, one way to annotate code

`/* Multi line comment*/` Anything that is between `/*` and `*/` will be treated as comment.

`int age = 19;` C++ requires you to manually set [data types for variables][cpp_data_types], int stands for integer, and can store 16 bits of data, ie. values between -2147483648 to 2147483647.

`float favouriteNumber = 2.718;` float is a [data type][cpp_data_types] aswel, which can store decimal values up to 7 digits.

`string name = "Seva";` string is a collection of characters, and can store 32 bits, which is 2^32 - 1 characters. String is anything that is between `"I am a sring"`.

`cout` is iostream method, used to output things into console, `print` is python equivalent. `<<` you can think of it as combine data to be displayed as one. For example `cout "I am " << age << "years old."` in python would be `print("I am ", age, " years old.")`. Last command `endl` means start a new line.

You may have noticed that I split previous command over multiple lines. Compiler knows that it's all one instruction because it is looking for `;` called "terminating character" to indicate end of the instruction.

`cin.ignore();` is again a iostream method, which is pausing program until Enter key has been pressed.

`return 0;` terminates main() function, and returns 0. Return code 0 means that everything went as expected, while others such as -1, 2, 101 etc. indicate that there was some kind of problem.

`}` and finally closing curly bracket indicates end of main function.


<b><u>Compilers</u></b>

There are many free C++ compilers, I personally like [Dev C++][dev_cpp] (Windows). One other obvious choice is [Microsoft Visual Studio][ms_cpp] (Windows) it supports variety of languages, C#, Python, VB, etc. as well as C++.

[Here][cpp_compilers_wiki] is more detailed list of compilers.

Majority of the compilers come with really powerful debuggers, and many more cool features, to help you build and fix your code faster.

<b><u>Some cool links</u></b>

[Very good book][cpp_book] explaining basics, and more advanced features of C++ using many examples and exercises.

[Website][cpp_website] dedicated to C++ programming.

[OpenGL][opengl_wiki] in C++ [tutorial][opengl_cpp_tutorial].

[cpp_problems]:https://www.quora.com/Why-is-C++-considered-a-bad-language
[methods_wiki]:https://en.wikipedia.org/wiki/Method_(computer_programming)
[libraries_wiki]:https://en.wikipedia.org/wiki/Library_(computing)
[cpp_website]:http://www.cplusplus.com/
[cpp_book]:http://freecomputerbooks.com/Object-Oriented-Programming-in-Cpp-3rd-Edition.html
[opengl_wiki]:https://en.wikipedia.org/wiki/OpenGL
[opengl_cpp_tutorial]:http://www.opengl-tutorial.org/beginners-tutorials/tutorial-1-opening-a-window/
[cpp_compilers_wiki]:https://en.wikipedia.org/wiki/List_of_compilers#C.2B.2B_compilers
[ms_cpp]:https://en.wikipedia.org/wiki/Microsoft_Visual_Studio
[dev_cpp]:https://en.wikipedia.org/wiki/Dev-C%2B%2B
[cpp_data_types]:http://www.tutorialspoint.com/cplusplus/cpp_data_types.htm
[mandelbrot_points]:https://en.wikipedia.org/wiki/Mandelbrot_set
[cpp_c_compatibility]:https://en.wikipedia.org/wiki/Compatibility_of_C_and_C%2B%2B
[cpp_tutorial]:https://www.google.co.uk/webhp?sourceid=chrome-instant&ion=1&espv=2&es_th=1&ie=UTF-8#q=c%2B%2B+tutorial
[cpp_memory_leaks]:https://en.wikipedia.org/wiki/Memory_leak
[cpp_pointers]:http://www.cplusplus.com/doc/tutorial/pointers/
[cpp_templates]:https://isocpp.org/wiki/faq/templates
[cpp_applications]:http://www.stroustrup.com/applications.html
[cpp_performace]:http://www.infoworld.com/article/2608770/application-development/application-development-stroustrup-why-the-35-year-old-c-still-dominates-real-dev.html
[popular_languages]:http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html
[stroutstrup_website_link]:http://www.stroustrup.com/index.html
