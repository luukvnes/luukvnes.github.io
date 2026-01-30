var interval = self.setInterval(() => {
  if (self.registration) {
    self.registration.showNotification('Hello from main script').catch((e) => {
      console.error(e)
      clearInterval(interval)
    })
  }
}, 10000)
