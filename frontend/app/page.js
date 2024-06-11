import Card from "@/components/Home/card";
import Footer from "@/components/Layout/footer";
import Navbar from "@/components/Layout/navbar";

export default function Home() {
  return (
    <>
      <Navbar />
      <div className="min-h-[82.5vh]">
        <div className="max-w-[1200px] mx-auto my-10 grid grid-cols-4 gap-10 ">
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
        </div>
      </div>
      <Footer />
    </>
  );
}
