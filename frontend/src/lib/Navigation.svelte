<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from "flowbite-svelte";
</script>

<Navbar fluid=true >
  <NavBrand href="/">
    <img src="/favicon.png" class="mr-3 h-6 sm:h-9" alt="Flowbite Logo" />
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite</span>
  </NavBrand>
  <NavHamburger  />
  <NavUl >
    <NavLi href="/">Home</NavLi>
    <NavLi href="/patients">Patient</NavLi>
    <NavLi href="/biopsies">Biopsies</NavLi>
    <NavLi href="/mutations">Mutations</NavLi>
    <NavLi href="/settings">Settings</NavLi>
  </NavUl>
</Navbar>