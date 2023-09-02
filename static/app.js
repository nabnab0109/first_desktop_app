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

    // 投稿の作成日時とカテゴリー名を表示
    const postDate = new Date(post.created_at).toLocaleString();
    const postCategory = post.category ? post.category.name : "Uncategorized";

    postElement.innerHTML = `
      <h3><a href="/posts/${post.id}">${post.title}</a></h3>
      <small>Posted on ${postDate} in ${postCategory}</small>
      <p>${post.content}</p>
    `;

    // 投稿をクリックしたら詳細ページに遷移
    postElement.addEventListener("click", () => {
      window.location.href = `/posts/${post.id}`;
    });

    postsContainer.appendChild(postElement);
  });
}
