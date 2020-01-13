<script>
  import LeaugeStandingsView from './LeaugeStandingsView.svelte';
  let leaugeId="726560"
</script>

<span>Enter leauge ID</span>
<input bind:value={leaugeId}>
<LeaugeStandingsView leaugeId={leaugeId}/>