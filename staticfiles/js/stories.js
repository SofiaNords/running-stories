document.addEventListener('DOMContentLoaded', (event) => {
  const editButtons = document.getElementsByClassName("btn-edit");
  const titleElement = document.getElementById("id_title");
  const excerptElement = document.getElementById("id_excerpt");
  const contentElement = document.getElementById("id_content");

  const storyForm = document.getElementById("storyForm");
  const submitButton = document.getElementById("submitButton");

  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let storyId = e.target.getAttribute("story_id");
      let storyTitle = document.getElementById(`story${storyId}`).innerText;
      titleElement.value = storyTitle
      storyExcerpt = document.getElementById(`storyExcerpt${storyId}`).innerText;
      excerptElement.value = storyExcerpt;
      let storyContent = document.getElementById(`storyContent${storyId}`).innerText;
      contentElement.value = storyContent;
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