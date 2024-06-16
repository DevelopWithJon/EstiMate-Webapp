"use client";
import { report } from "@/app/data/report";
import Footer from "@/components/Layout/footer";
import Navbar from "@/components/Layout/navbar";
import AnalysisCard from "@/components/Report/analysisCard";
import { chartjs } from "chart.js/auto";
import { Doughnut, Line } from "react-chartjs-2";

export default function Page({ params }) {
  const data = report;
  const item = data.find((item) => item.propertyId === params.id);
  const graphLabels = [
    "Year 1",
    "Year 2",
    "Year 3",
    "Year 4",
    "Year 5",
    "Year 6",
    "Year 7",
    "Year 8",
    "Year 9",
    "Year 10",
  ];
  const datasets = [
    {
      label: "Revenue",
      data: item.all_revenue,
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
      borderWidth: 1,
    },
  ];
  const keys = [
    "year_one_cap",
    "unlevered_irr",
    "levered_irr",
    "unleveredmom",
    "levered_mom",
    "levered_profit",
  ];
  return (
    <>
      <Navbar />
      <div className="min-h-[87vh]">
        <div className="max-w-[1200px] mx-auto my-10 grid grid-cols-4 gap-5 ">
          {keys.map((each, id) => (
            <AnalysisCard key={id} title={each} value={item[each].toFixed(2)} />
          ))}
        </div>
        <h1 className="text-center text-[30px] font-semibold text-black m-[50px]">
          Monthy Expense Pie chart
        </h1>
        <div className="flex justify-center w-[30vw] h-auto m-auto">
          <Doughnut
            data={{
              labels: [
                "water",
                "electricity",
                "gas",
                "capex",
                "HOA",
                "Insurance",
                "utilities",
                "management",
              ],
              datasets: [
                {
                  label: "Expense",
                  data: [
                    item.water,
                    item.electricity,
                    item.gas,
                    item.capex,
                    item.HOA,
                    item.insurance,
                    item.utilities,
                    item.management,
                  ],
                  backgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#FF6360",
                    "#4BC0C0",
                    "#9966FF",
                    "#FF9F40",
                    "#FFCD96",
                  ],
                  hoverBackgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#FF6360",
                    "#4BC0C0",
                    "#9966FF",
                    "#FF9F40",
                    "#FFCD56",
                  ],
                  borderRadius: 8,
                  borderWidth: 2,
                },
              ],
            }}
          />
        </div>
        <div className="w-[50vw] h-auto mx-auto my-10">
          <h1 className="text-center text-[30px] font-semibold text-black m-[30px]">
            Revenue Line chart
          </h1>
          <Line
            data={{
              labels: graphLabels,
              datasets: datasets,
            }}
          />
        </div>
      </div>
      <Footer />
    </>
  );
}
