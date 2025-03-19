const API_BASE_URL =
  'http://ec2-3-37-128-206.ap-northeast-2.compute.amazonaws.com/api'
let currentUser = null
let authToken = null

// API 요청에 공통으로 사용할 헤더를 생성하는 함수
function getHeaders() {
  const headers = {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  }
  if (authToken) {
    headers['Authorization'] = `Token ${authToken}`
  }
  return headers
}

// 인증 관련 함수들
async function register() {
  const username = document.getElementById('username').value
  const password = document.getElementById('password').value

  try {
    const response = await fetch(`${API_BASE_URL}/users/register/`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ username, password }),
      credentials: 'include',
    })

    if (response.ok) {
      alert('회원가입이 완료되었습니다. 로그인해주세요.')
    } else {
      const data = await response.json()
      alert(data.message || '회원가입에 실패했습니다.')
    }
  } catch (error) {
    console.error('Error:', error)
    alert('회원가입 중 오류가 발생했습니다.')
  }
}

async function login() {
  const username = document.getElementById('username').value
  const password = document.getElementById('password').value

  try {
    const response = await fetch(`${API_BASE_URL}/users/login/`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ username, password }),
      credentials: 'include',
    })

    if (response.ok) {
      const data = await response.json()
      currentUser = username
      authToken = data.token
      updateAuthUI()
      loadArticles()
    } else {
      const data = await response.json()
      alert(data.message || '로그인에 실패했습니다.')
    }
  } catch (error) {
    console.error('Error:', error)
    alert('로그인 중 오류가 발생했습니다.')
  }
}

async function logout() {
  try {
    const response = await fetch(`${API_BASE_URL}/users/logout/`, {
      method: 'POST',
      headers: getHeaders(),
      credentials: 'include',
    })

    if (response.ok) {
      currentUser = null
      authToken = null
      updateAuthUI()
      loadArticles()
    }
  } catch (error) {
    console.error('Error:', error)
    alert('로그아웃 중 오류가 발생했습니다.')
  }
}

function updateAuthUI() {
  const loginForm = document.getElementById('login-form')
  const userInfo = document.getElementById('user-info')
  const userName = document.getElementById('user-name')
  const articleForm = document.querySelector('.article-form')

  if (currentUser) {
    loginForm.classList.add('hidden')
    userInfo.classList.remove('hidden')
    userName.textContent = currentUser
    articleForm.classList.remove('hidden')

    // 입력 필드 초기화
    document.getElementById('username').value = ''
    document.getElementById('password').value = ''
  } else {
    loginForm.classList.remove('hidden')
    userInfo.classList.add('hidden')
    userName.textContent = ''
    articleForm.classList.add('hidden')
  }
}

// 게시글 관련 함수들
async function loadArticles() {
  try {
    const response = await fetch(`${API_BASE_URL}/articles/`, {
      headers: getHeaders(),
      credentials: 'include',
    })

    if (response.ok) {
      const articles = await response.json()
      displayArticles(articles)
    } else {
      console.error('Failed to load articles')
    }
  } catch (error) {
    console.error('Error:', error)
  }
}

function displayArticles(articles) {
  const container = document.getElementById('articles-container')
  container.innerHTML = ''

  articles.forEach((article) => {
    const articleElement = document.createElement('div')
    articleElement.className = 'article'
    articleElement.innerHTML = `
                <h2>${article.title}</h2>
                <p>${article.content}</p>
                ${
                  currentUser === article.author
                    ? `
                    <div class="article-actions">
                        <button onclick="editArticle(${article.id})">수정</button>
                        <button onclick="deleteArticle(${article.id})">삭제</button>
                    </div>
                `
                    : ''
                }
            `
    container.appendChild(articleElement)
  })
}

async function createArticle() {
  const title = document.getElementById('article-title').value
  const content = document.getElementById('article-content').value

  if (!title || !content) {
    alert('제목과 내용을 모두 입력해주세요.')
    return
  }

  try {
    const response = await fetch(`${API_BASE_URL}/articles/`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ title, content }),
      credentials: 'include',
    })

    if (response.ok) {
      document.getElementById('article-title').value = ''
      document.getElementById('article-content').value = ''
      loadArticles()
    } else {
      const data = await response.json()
      alert(data.message || '게시글 작성에 실패했습니다.')
    }
  } catch (error) {
    console.error('Error:', error)
    alert('게시글 작성 중 오류가 발생했습니다.')
  }
}

async function editArticle(id) {
  const newTitle = prompt('새로운 제목을 입력하세요:')
  const newContent = prompt('새로운 내용을 입력하세요:')

  if (!newTitle || !newContent) return

  try {
    const response = await fetch(`${API_BASE_URL}/articles/${id}/`, {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify({ title: newTitle, content: newContent }),
      credentials: 'include',
    })

    if (response.ok) {
      loadArticles()
    } else {
      const data = await response.json()
      alert(data.message || '게시글 수정에 실패했습니다.')
    }
  } catch (error) {
    console.error('Error:', error)
    alert('게시글 수정 중 오류가 발생했습니다.')
  }
}

async function deleteArticle(id) {
  if (!confirm('정말로 이 게시글을 삭제하시겠습니까?')) return

  try {
    const response = await fetch(`${API_BASE_URL}/articles/${id}/`, {
      method: 'DELETE',
      headers: getHeaders(),
      credentials: 'include',
    })

    if (response.ok) {
      loadArticles()
    } else {
      const data = await response.json()
      alert(data.message || '게시글 삭제에 실패했습니다.')
    }
  } catch (error) {
    console.error('Error:', error)
    alert('게시글 삭제 중 오류가 발생했습니다.')
  }
}

// 초기 로드
document.addEventListener('DOMContentLoaded', () => {
  updateAuthUI()
  loadArticles()
})
