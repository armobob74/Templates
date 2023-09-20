function setCookie(cookie_name, cookie_value) {
  const expirationDate = new Date();
  expirationDate.setFullYear(expirationDate.getFullYear() + 10); // Set the expiration date to 10 years from now
  
  const expires = "expires=" + expirationDate.toUTCString();
  document.cookie = `${cookie_name}=${cookie_value};${expires};path=/`;
}

function getCookie(cookie_name) {
  const name = cookie_name + "=";
  const decodedCookie = decodeURIComponent(document.cookie);
  const cookieArray = decodedCookie.split(';');
  
  for (let i = 0; i < cookieArray.length; i++) {
    let cookie = cookieArray[i];
    while (cookie.charAt(0) === ' ') {
      cookie = cookie.substring(1);
    }
    if (cookie.indexOf(name) === 0) {
      return cookie.substring(name.length, cookie.length);
    }
  }
  
  return "";
}

function cookieExists(cookie_name) {
  return getCookie(cookie_name) !== "";
}

