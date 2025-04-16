# Clickjacking Awareness Project

This is a basic demonstration project built to understand how **clickjacking** attacks work and how we can protect web applications against them.

## 🚨 What is Clickjacking?
Clickjacking is a malicious technique where an attacker tricks a user into clicking something different from what the user perceives, by hiding malicious elements over a legitimate page using layers, opacity, or iframes.

## 📂 Project Structure
```
Clickjacking-Project/
├── Attacker/
│   └── index.html      # Malicious page with iframe and overlay button
├── Victim/
│   ├── index.html      # Legitimate login form
│   └── welcome.html    # Page shown after successful login
└── README.md           # This file
```

## 🎯 Victim Page Features
- Simple login UI with dark-themed styling
- Form submission redirects to `welcome.html`

## 🧨 Attacker Page Features
- Embeds the victim page inside an iframe
- Adds a low-opacity malicious button over the login button to simulate a clickjacking attack

### Sample Attacker Overlay Button
```html
<button class="malicious-button" onclick="doMaliciousThing()">
  Malicious Redirect
</button>
```

## 🛡️ Prevention Techniques
### 1. **JavaScript Frame Busting**
```js
if (window.top !== window.self) {
  window.top.location = window.self.location;
}
```

### 2. **HTTP Response Headers**
Add these headers from your server:
```http
X-Frame-Options: DENY or SAMEORIGIN
```
or
```http
Content-Security-Policy: frame-ancestors 'none';
```

### 3. **UI Defense Layers**
- Avoid using static z-index-based buttons without pointer isolation
- Use `pointer-events: none` for suspected iframe overlays (in combination with JavaScript checks)

## 🧠 What I Learned
This project was built as part of my self-study in web security. By simulating both attacker and victim perspectives, I gained a deeper understanding of how front-end security plays a role in defending users.

## 🚀 Try It Yourself
You can open the `Victim/index.html` in a browser to see the normal login flow. Then open `Attacker/index.html` to see how an attacker might try to hijack user clicks.

> ⚠️ Note: This is a simulated demo project for awareness purposes only.

---


