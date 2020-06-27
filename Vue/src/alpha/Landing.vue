<template>
  <div>
    <Header />
    <Main />
    <Features />
    <WhyUs />
    <ContactUs />
    <Footer />
  </div>
</template>

<script>
import Header from "./Header";
import Features from "./Features";
import ContactUs from "./ContactUs";
import Footer from "./Footer";
import Main from "./Main";
import WhyUs from "./WhyUs";

export default {
  components: {
    Header,
    Main,
    Features,
    WhyUs,
    ContactUs,
    Footer
  }
};
</script>

