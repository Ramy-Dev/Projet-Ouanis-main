export function clickOutside(node, { enabled: initialEnabled, callback }) {
  const handleClick = (event) => {
    if (!node.contains(event.target)) {
      callback();
    }
  };

  function update({ enabled }) {
    if (enabled) {
      // Add a small delay before attaching the event listener
      setTimeout(() => {
        document.addEventListener('click', handleClick);
      }, 0);
    } else {
      document.removeEventListener('click', handleClick);
    }
  }

  update({ enabled: initialEnabled });

  return {
    update,
    destroy() {
      document.removeEventListener('click', handleClick);
    }
  };
}