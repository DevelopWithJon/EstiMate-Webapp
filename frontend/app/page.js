import Card from "@/components/Home/card";
import Footer from "@/components/Layout/footer";
import Navbar from "@/components/Layout/navbar";
import { report } from "./data/report";

export default function Home() {
  const data = report;
  return (
    <>
      <Navbar />
      <div className="min-h-[82.5vh]">
        <div className="max-w-[1200px] mx-auto my-10 grid grid-cols-4 gap-10 ">
          {data.map((item , id) => (
            <Card key={id} item={item} />
          ))}
        </div>
      </div>
      <Footer />
    </>
  );
}
