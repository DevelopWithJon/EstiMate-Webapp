import Link from "next/link";
import house from "@/public/house.png";
import Image from "next/image";

export default function Card({item}) {
  return (
    <div className="card max-w-96 shadow-xl text-black">
      <figure>
        <Image className="h-[200px]" src={item.image} alt="house img" width={250} height={150}/>
      </figure>
      <div className="card-body p-5">
        <h2 className="card-title">{item.propertyId}</h2>
        <p>{item.address}</p>
        <div className="card-actions justify-end">
          <Link href={`/report/${item.propertyId}`}>
            <div className="badge badge-outline hover:bg-[#1990FF] p-[13px] hover:cursor-pointer hover:text-white">
              More Info
            </div>
          </Link>
          <div className="badge badge-outline hover:bg-[#FF5761] p-[13px] hover:cursor-pointer hover:text-white">
            Delete
          </div>
        </div>
      </div>
    </div>
  );
}
