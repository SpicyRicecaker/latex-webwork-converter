<script>
	let latex = '';
	let webwork = '';

	const rules = [
		[`c_{1}`, 'c1'],
		[`c_{2}`, 'c2'],
		[String.raw`left`, ''],
		[String.raw`right`, ''],
		[String.raw`_`, ''],
		['\\', ''],
		// multiply
		[String.raw`cdot`, '*'],
		// division
		[String.raw`frac{`, '('],
		[String.raw`}{`, ')/('],
		// cleanup all remaining curly brackets
		// make sure this is at the end
		[String.raw`{`, '('],
		[String.raw`}`, ')']
	];

	$: {
		let temp = latex;
		for (let i = 0; i < rules.length; i++) {
			temp = temp.replaceAll(rules[i][0], rules[i][1]);
		}
		webwork = temp;
	}
</script>

<svelte:head>
	<title>Webwork Converter</title>
	<meta name="description" content="Latex to Webwork Converter!" />
	<style>
		@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap');
	</style>
</svelte:head>

<section>
	<h1>
		<div style="color: #a9b665">Desmos</div>
		<div style="opacity: 50%">to</div>
		<div><span style="color: #7daea3">Webwork </span>Converter</div>
	</h1>
	<label>
		<input class="roboto-mono-input" placeholder="paste from desmos here..." bind:value={latex} />
	</label>
	<div style="align-self: center">▼</div>
	<label>
		<input class="roboto-mono-input" readonly bind:value={webwork} />
	</label>
	<div style="align-self: center; width: 60vw; opacity: 70%;">
		*Please put a parenthesis around arguments for sin and cos in Desmos, as sin2x will be evaluated by Webwork as sin(2)*x
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: left;
		align-self: center;
		gap: 1rem;
		flex: 0.6;
	}

	h1 {
		font-size: 2rem;
		margin: 0;
		text-align: left;
	}

	.roboto-mono-input {
		font-family: 'Roboto Mono', monospace;
		font-optical-sizing: auto;
		font-weight: 400;
		font-style: normal;
	}

	input {
		padding: 0.6rem;
		margin: 0;
		width: 60vw;

		background-color: #504945;
		outline: none;
		border-radius: 4px;
		color: var(--color-text);

		border: 2px solid var(--color-bg-1);
	}
	input:focus {
		border: 2px solid var(--color-text);
	}

	::selection {
		background: #d8a657;
		color: #141617;
	}

	::placeholder {
		color: var(--color-text);
		opacity: 50%;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
