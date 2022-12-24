import os

def main():
    directory_input = raw_input("Input the directory (absolute) for CMake project: ") 
    name_input = raw_input("Enter CMakeList Project Name: ")
    cmake_min_version = raw_input("Min. CMake version number: ")
    cmake_cxx_lang_ver = raw_input("Min. required CXX language version: ")
    project_version_num = raw_input("Initial project ver. number: ")
    print("Project created at :" + directory_input + "/" + name_input)
    path = os.path.join(directory_input, name_input)
    if not os.path.isExist(path):
        os.mkdir(path)
    else:
        cmake_file_path = os.path.join(path, "CMakeList.txt")
        with (open file_path, "a+") as existing_cmake_file:
            # Just keeping this here in case there is a use-case cannot see one yet. 
            # Usually we will just create a new CMakeLists file each time so this shouldn't
            # really need to be used but we'll see. 
            pass

    # Boilerplate CMake Generation Step
    print("========== Creating Boilerplate CMakeLists File ==========")
    file_path = os.path.join(path, "CMakeLists.txt")
    with open(file_path, "w+") as cmake_file:
        cmake_file.write("cmake_minimum_required_version(VERSION "+cmake_min_version+")\n")
        cmake_file.write("set(CMAKE_CXX_STANDARD "+cmake_cxx_lang_ver+")\n")
        cmake_file.write("set(CMAKE_CXX_STANDARD_REQUIRED TRUE)\n")
        print("========== Writing Project Specifics ==========")
        cmake_file.write("project (\n")
        cmake_file.write("    "+name_input+"\n")
        cmake_file.write("    LANGUAGES CXX\n")
        cmake_file.write("    VERSION "+project_version_num+"\n")
        cmake_file.write(")")
 

if __name__ == '__main__':
    main()
