"""
1. Endpoint được khai báo trong chương trình là: GET /student.

2. Nếu truy cập GET /students sẽ nhận lỗi 404 Not Found,
   do ứng dụng chưa định nghĩa endpoint có đường dẫn /students.

3. Đường dẫn /student chưa hợp lý vì API này dùng để lấy nhiều sinh viên.
   Theo quy ước REST nên đặt tên ở dạng số nhiều: /students.

4. Câu lệnh return students[0] chỉ trả về thông tin của sinh viên đầu tiên,
   nên chưa đáp ứng yêu cầu trả về toàn bộ danh sách.

5. Để đúng với yêu cầu, API nên được khai báo là:
   GET /students và trả về toàn bộ biến students.
"""

from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"}
]

@app.get("/students")
def get_students():
    return students
