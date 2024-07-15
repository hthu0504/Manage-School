from Classroom.Student import Student

from manage import manage

def main():
    while True:
        print("\nMenu:")
        print("1. Thêm học sinh")
        print("2. Xóa học sinh")
        print("3. Thêm giáo viên")
        print("4. Xóa giáo viên")
        print("5. Thêm lớp học")
        print("6. Xóa lớp học")
        print("7. Thoát")
        
        choice = input("Chọn tùy chọn: ")
        
        hi = manage()
        if choice == '1':
            name = input("Nhập tên học sinh: ")
            lop = input("Nhập lớp: ")
            birth = input("Nhập năm sinh: ")
            hi.AddStudent(name, lop, birth)
        
        elif choice == '2':
            name = input("Nhập tên học sinh: ")
            lop = input("Nhập lớp: ")
            birth = input('Năm sinh: ')
            hi.RemoveStudent(name, birth, lop)
        
        elif choice == '3':
            name = input("Nhập tên giáo viên: ")
            subj = input("Nhập môn học: ")
            lop = input("Nhập lớp: ")
            birth = input("Nhập năm sinh: ")
            hi.AddTeacher(name, subj, lop, birth)

        elif choice == '4':
            name = input("Nhập tên giáo viên: ")
            birth = input("Nhập năm sinh: ")
            lop = input('Xóa khỏi lớp: ')
            hi.RemoveTeacher(name, birth, lop)

        elif choice == '5':
            name = input('Nhập tên lớp: ')
            khoa = input('Nhập khóa: ')
            hi.AddClass(name, khoa)

        elif choice == '6':
            name = input('Xóa lớp: ')
            khoa = input('Nhập khóa: ')
            hi.RemoveClass(name, khoa)
        
        elif choice == '7':
            print("Thoát chương trình")
            break
        
        else:   
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()


