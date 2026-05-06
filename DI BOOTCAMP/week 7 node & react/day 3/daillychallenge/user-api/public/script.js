// REGISTER FORM
const regInputs = ["name", "lastName", "email", "username", "password"];
const regBtn = document.getElementById("registerBtn");

if (regBtn) {
  regInputs.forEach(id => {
    document.getElementById(id).addEventListener("input", checkRegister);
  });

  function checkRegister() {
    const empty = regInputs.some(id => !document.getElementById(id).value);
    regBtn.disabled = empty;
  }

  document.getElementById("registerForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      name: name.value,
      lastName: lastName.value,
      email: email.value,
      username: username.value,
      password: password.value
    };

    const res = await fetch("/api/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    document.getElementById("msg").innerText = result.message;
  });
}


// LOGIN FORM
const loginBtn = document.getElementById("loginBtn");

if (loginBtn) {
  ["loginUsername", "loginPassword"].forEach(id => {
    document.getElementById(id).addEventListener("input", checkLogin);
  });

  function checkLogin() {
    const u = document.getElementById("loginUsername").value;
    const p = document.getElementById("loginPassword").value;
    loginBtn.disabled = !u || !p;
  }

  document.getElementById("loginForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      username: loginUsername.value,
      password: loginPassword.value
    };

    const res = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    document.getElementById("msg").innerText = result.message;
  });
}