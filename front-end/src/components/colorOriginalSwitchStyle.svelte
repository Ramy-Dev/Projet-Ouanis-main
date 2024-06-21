<script>
  export let color;

</script>

<!-- Appliquez les styles en fonction de la couleur -->
<main>
  {#if color === "#5A02D4"}
    <style>
      .colorOriginalSwitch {
        background-color: #f5f5f5;
        color: #5a02d4;
        border: 4px solid #5a02d4;
        box-shadow: none !important;
        transition-property: none !important;
      }
      .categorieTarifCard {
        color: #27005d;
      }
    </style>
  {:else if color === "#27005D"}
    <style>
      .colorOriginalSwitch {
        background-color: #f5f5f5;
        color: #5a02d4;
        border: 4px solid #27005d;
        box-shadow: none !important;
        transition-property: none !important;
      }
      .categorieTarifCard {
        color: #27005d;
      }
    </style>
  {:else if color === "#FFE767"}
    <style>
      .colorOriginalSwitch {
        background-color: #f5f5f5;
        color: #27005d;
        border: 4px solid #ffe767;
        box-shadow: none !important;
        transition-property: none !important;
      }
      .categorieTarifCard {
        color: #5a02d4;
      }
    </style>
  {:else if color === "#84BBFF"}
    <style>
      .colorOriginalSwitch {
        background-color: #f5f5f5;
        color: #5a02d4;
        border: 4px solid #84bbff;
        box-shadow: none !important;
        transition-property: none !important;
      }
      .categorieTarifCard {
        color: #27005d;
      }
    </style>
  {:else if color === "#BFACFE"}
    <style>
      .colorOriginalSwitch {
        background-color: #f5f5f5;
        color: #5a02d4;
        border: 4px solid #bfacfe;
        box-shadow: none !important;
        transition-property: none !important;
      }
      .categorieTarifCard {
        color: #27005d;
      }
    </style>
  {/if}
  </main>
