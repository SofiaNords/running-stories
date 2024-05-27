document.addEventListener('DOMContentLoaded', (event) => {

  // Get all edit buttons
  const editButtons = document.getElementsByClassName("btn-edit");

  // Get form elements
  const titleElement = document.getElementById("id_title");
  const excerptElement = document.getElementById("id_excerpt");
  const contentElement = document.getElementById("id_content");

  // Get story form and submit button
  const storyForm = document.getElementById("storyForm");
  const submitButton = document.getElementById("submitButton");

  // Create a modal for delete confirmation
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

  // Get all delete buttons
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  // Add event listeners for edit buttons
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let storyId = e.target.getAttribute("story_id");
      let storyTitle = document.getElementById(`story${storyId}`).innerText;
      titleElement.value = storyTitle;
      let storyExcerpt = document.getElementById(`storyExcerpt${storyId}`).innerText;
      excerptElement.value = storyExcerpt;
      let storyContent = document.getElementById(`storyContent${storyId}`).innerText;
      contentElement.value = storyContent;
      submitButton.innerText = "Update";
      storyForm.setAttribute("action", `edit_story/${storyId}`);
    });
  }

  // Add event listeners for delete buttons
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let storyId = e.target.getAttribute("story_id");
      deleteConfirm.href = `story_delete/${storyId}`;
      deleteModal.show();
    });
  }
});