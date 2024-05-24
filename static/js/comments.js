// Get all edit buttons
const editButtons = document.getElementsByClassName("btn-edit");

// Get the comment text area
const commentText = document.getElementById("id_body");

// Get the comment form
const commentForm = document.getElementById("commentForm");

// Get the submit button
const submitButton = document.getElementById("submitButton");

// Create a modal for delete confirmation
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

// Get all delete buttons
const deleteButtons = document.getElementsByClassName("btn-delete");

// Get the delete confirmation link
const deleteConfirm = document.getElementById("deleteConfirm");

// Add event listeners for edit buttons
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

// Add event listeners for delete buttons
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }