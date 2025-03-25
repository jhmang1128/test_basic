// 백엔드 API 주소
const API_BASE = "http://127.0.0.1:8000/post/";

const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyODUzNDMyLCJpYXQiOjE3NDI4MzU0MzIsImp0aSI6ImM2NzNmZWIyYTE2MjRkM2I4NWIzOWQ1OGJlNWY5YjJhIiwidXNlcl9pZCI6Mn0.m31uVhVyuaywcT21n1fWd5m5ORoCSyQEhcHzAKqSzak"

// 새 게시글 작성
document.getElementById("post_create").addEventListener("submit", async (e) => {
    e.preventDefault();
    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;
    await fetch(API_BASE + "create/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ title, content })
    });
});
