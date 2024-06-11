import Link from "next/link";
import house from "@/public/house.png";
import Image from "next/image";

export default function Card() {
  return (
    <div className="card max-w-96 shadow-xl text-black">
      <figure>
        <Image src={house} alt="house img" />
      </figure>
      <div className="card-body p-5">
        <h2 className="card-title">House Name!</h2>
        <p>This is a very good house that you need to buy</p>
        <div className="card-actions justify-end">
          <Link href="/report">
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
