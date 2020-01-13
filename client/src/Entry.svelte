<script>
    export let entry;
    export let maxScore;
</script>

<style>
	div {
        position: absolute;
        display: flex;
        white-space: nowrap;
	}
</style>

<div style="top: {(maxScore-entry.total)*5}px;">
    <span>{entry.rank}</span>
    <span>{entry.player_name}</span>
    <span>{entry.entry_name}</span>
    <span>{entry.total}</span>
</div>