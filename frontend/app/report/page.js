"use client"
import Footer from "@/components/Layout/footer";
import Navbar from "@/components/Layout/navbar";
import AnalysisCard from "@/components/Report/analysisCard";
import {chartjs} from 'chart.js/auto'
import { Doughnut } from "react-chartjs-2";

export default function Report() {
  return (
    <>
      <Navbar />
      <div className="min-h-[87vh]">
        <div className="max-w-[1200px] mx-auto my-10 grid grid-cols-4 gap-5 ">
            <AnalysisCard title="Total Profit" value="₹ 1,00,000" profit={true}/>
            <AnalysisCard title="Total Profit" value="₹ 1,00,000" profit={true}/>
            <AnalysisCard title="Total Loss" value="₹ 1,00,000" />
            <AnalysisCard title="Total Profit" value="₹ 1,00,000" profit={true}/>
            <AnalysisCard title="Total Profit" value="₹ 1,00,000" profit={true}/>
            <AnalysisCard title="Total Loss" value="₹ 1,00,000" />
            <AnalysisCard title="Total Loss" value="₹ 1,00,000" />
            <AnalysisCard title="Total Loss" value="₹ 1,00,000" />
            <AnalysisCard title="Total Profit" value="₹ 1,00,000" profit={true}/>
            <AnalysisCard title="Total Loss" value="₹ 1,00,000" />
        </div>
        <h1 className="text-center text-[30px] font-semibold text-black m-[50px]">Monthy Expense Pie chart</h1>
          <div className="w-[30vw] m-auto">
            <Doughnut
              data={{
                labels: ["Rent", "Salary", "Grocery", "Others"],
                datasets: [
                  {
                    label: "Expense",
                    data: [1000, 2000, 3000, 4000],
                    backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#FF6360"],
                    hoverBackgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#FF6384"],
                    borderRadius: 8,
                    borderWidth: 2,
                  },
                ],
              }}
            />
          </div>
      </div>
      <Footer />
    </>
  );
}
