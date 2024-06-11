import Image from "next/image";
import profitLogo from "@/public/profitLogo.png";
import lossLogo from "@/public/loss.png";

export default function AnalysisCard({ title, value , profit}) {
  return (
    <div className="bg-gray-200 p-8 flex gap-8 rounded-lg">
      <div className="flex flex-col gap-4">
        <h1 className="text-[22px] text-black font-semibold">{title}</h1>
        <h2 className="text-[20px] text-black ">{value}</h2>
      </div>
      <div>
        <Image src={profit ? profitLogo : lossLogo} alt="img" width={70} height={70} />
      </div>
    </div>
  );
}
