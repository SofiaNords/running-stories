document.addEventListener('DOMContentLoaded', (event) => {
  const editButtons = document.getElementsByClassName("btn-edit");
  const titleStory = document.getElementById("title");
  const excerptStory = document.getElementById("excerpt");
  const contentStory = document.getElementById("content");

  const storyForm = document.getElementById("storyForm");
  const submitButton = document.getElementById("submitButton");

  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let storyId = e.target.getAttribute("story_id");
      let storyTitleText = document.getElementById(`storyTitle${storyId}`).innerText;
      titleStory.value = storyTitleText;
      let storyExcerptText = document.getElementById(`storyExcerpt${storyId}`).innerText;
      excerptStory.value = storyExcerptText;
      let storyContentText = document.getElementById(`storyContent${storyId}`).innerText;
      contentStory.value = storyContentText;
      submitButton.innerText = "Update";
      storyForm.setAttribute("action", `edit_story/${storyId}`);
    });
  }

  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let storyId = e.target.getAttribute("story_id");
      deleteConfirm.href = `story_delete/${storyId}`;
      deleteModal.show();
    });
  }
});