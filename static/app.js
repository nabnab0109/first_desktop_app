document.addEventListener("DOMContentLoaded", () => {
  fetchLatestPosts();
});

async function fetchLatestPosts() {
  const response = await fetch("/api/posts");
  const data = await response.json();

  const postsContainer = document.querySelector(".posts");
  data.forEach(post => {
    const postElement = document.createElement("div");
    postElement.classList.add("post");
    postElement.innerHTML = `
      <h3>${post.title}</h3>
      <p>${post.content}</p>
    `;
    postsContainer.appendChild(postElement);
  });
}
