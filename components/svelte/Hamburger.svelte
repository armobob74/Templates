<script>
	function toggleActive(){
		let btn = document.querySelector('.btn');
		btn.classList.toggle('active');
		btn.classList.toggle('not-active');
	}
</script>
<button class="hamburger" on:click={toggleActive}>
	<div class="btn not-active">
		<span></span>
		<span></span>
		<span></span>
	</div>
</button>
<style>
  /* Defining CSS Variables */
  :root {
    --bar-height: 4px;
    --bar-gap: 6px;
    --bar-color: black;
    --move-len: calc(var(--bar-height) + var(--bar-gap));
  }

  .hamburger {
    background: none;
    border:none;
  }

  .btn {
    width: 24px;
    cursor: pointer;
  }

  span {
    display: block;
    width: 100%;
    border-radius: 3px;
    height: var(--bar-height);
    background: var(--bar-color);
    transition: all .3s;
    position: relative;
  }

  span + span {
    margin-top: var(--bar-gap);
  }

  .active span:nth-child(1) {
    animation: ease .7s top forwards;
  }

  .not-active span:nth-child(1) {
    animation: ease .7s top-2 forwards;
  }

  .active span:nth-child(2) {
    animation: ease .7s scaled forwards;
  }

  .not-active span:nth-child(2) {
    animation: ease .7s scaled-2 forwards;
  }

  .active span:nth-child(3) {
    animation: ease .7s bottom forwards;
  }

  .not-active span:nth-child(3) {
    animation: ease .7s bottom-2 forwards;
  }

  @keyframes top {
    0% {
      transform: rotate(0);
    }
    50% {
      top: var(--move-len);
      transform: rotate(0);
    }
    100% {
      top: var(--move-len);
      transform: rotate(45deg);
    }
  }

  @keyframes top-2 {
    0% {
      top: var(--move-len);
      transform: rotate(45deg);
    }
    50% {
      top: var(--move-len);
      transform: rotate(0deg);
    }
    100% {
      top: 0;
      transform: rotate(0deg);
    }
  }

  @keyframes bottom {
    0% {
      bottom: 0;
      transform: rotate(0);
    }
    50% {
      bottom: var(--move-len);
      transform: rotate(0);
    }
    100% {
      bottom: var(--move-len);
      transform: rotate(135deg);
    }
  }

  @keyframes bottom-2 {
    0% {
      bottom: var(--move-len);
      transform: rotate(135deg);
    }
    50% {
      bottom: var(--move-len);
      transform: rotate(0);
    }
    100% {
      bottom: 0;
      transform: rotate(0);
    }
  }

  @keyframes scaled {
    0% {
      transform: scale(1);
    }
    25% {
      transform: scale(1);
    }
    50% {
      transform: scale(0);
    }
    100% {
      transform: scale(0);
    }
  }

  @keyframes scaled-2 {
    0% {
      transform: scale(0);
    }
    50% {
      transform: scale(0);
    }
    100% {
      transform: scale(1);
    }
  }
</style>
