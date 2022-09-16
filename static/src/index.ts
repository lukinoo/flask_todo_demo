const form_input = document.getElementById("todo__input") as HTMLInputElement;
const form_button = document.getElementById(
  "todo__button"
) as HTMLButtonElement;

// button disable handler
const inputHandler = (): void => {
  let { value } = form_input;

  if (!value.trim()) {
    form_button.disabled = true;
  } else {
    form_button.disabled = false;
  }
};

// input event
form_input.addEventListener("input", inputHandler);
