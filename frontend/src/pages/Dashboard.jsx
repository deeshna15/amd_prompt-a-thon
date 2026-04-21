import { useState, useEffect } from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import { Activity, Flame, Droplets, Target, TrendingUp, Award } from 'lucide-react';

const COLORS = ['#10b981', '#f1f5f9']; // Emerald and Slate
const MACRO_COLORS = {
  protein: '#3b82f6', // Blue
  carbs: '#f59e0b', // Amber
  fat: '#ef4444' // Red
};

export default function Dashboard() {
  const [healthScore, setHealthScore] = useState(85);
  const [streak, setStreak] = useState(12);

  const scoreData = [
    { name: 'Score', value: healthScore },
    { name: 'Remaining', value: 100 - healthScore }
  ];

  const macroData = [
    { name: 'Protein', value: 85, fill: MACRO_COLORS.protein },
    { name: 'Carbs', value: 120, fill: MACRO_COLORS.carbs },
    { name: 'Fat', value: 45, fill: MACRO_COLORS.fat },
  ];

  const weeklyTrends = [
    { day: 'Mon', score: 75 },
    { day: 'Tue', score: 82 },
    { day: 'Wed', score: 88 },
    { day: 'Thu', score: 85 },
    { day: 'Fri', score: 90 },
    { day: 'Sat', score: 80 },
    { day: 'Sun', score: 85 },
  ];

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-8 animate-in fade-in duration-500">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-slate-800">Hello, User! 👋</h1>
          <p className="text-slate-500 mt-1">Here is your health summary for today.</p>
        </div>
        <div className="flex items-center gap-2 bg-amber-100 text-amber-700 px-4 py-2 rounded-full font-bold">
          <Flame size={20} className="text-amber-500" />
          <span>{streak} Day Streak!</span>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Health Score Gauge */}
        <div className="bg-white rounded-3xl p-6 shadow-sm border border-slate-100 flex flex-col items-center justify-center relative overflow-hidden group">
          <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-emerald-400 to-teal-500"></div>
          <h3 className="text-lg font-semibold text-slate-700 mb-4 w-full flex items-center gap-2">
            <Activity className="text-emerald-500" /> Health Score
          </h3>
          <div className="h-48 w-full relative">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={scoreData}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={80}
                  startAngle={90}
                  endAngle={-270}
                  dataKey="value"
                  stroke="none"
                  cornerRadius={10}
                >
                  {scoreData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
              </PieChart>
            </ResponsiveContainer>
            <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
              <span className="text-4xl font-black text-slate-800">{healthScore}</span>
              <span className="text-sm text-slate-500 font-medium">/ 100</span>
            </div>
          </div>
          <p className="text-center text-sm text-slate-600 mt-2 bg-slate-50 p-3 rounded-xl">
            "Great job! Your protein intake is optimal today."
          </p>
        </div>

        {/* Macros Bar Chart */}
        <div className="bg-white rounded-3xl p-6 shadow-sm border border-slate-100">
          <h3 className="text-lg font-semibold text-slate-700 mb-4 flex items-center gap-2">
            <Target className="text-blue-500" /> Macros Tracker
          </h3>
          <div className="h-48 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={macroData} layout="vertical" margin={{ top: 0, right: 0, left: 0, bottom: 0 }}>
                <XAxis type="number" hide />
                <YAxis dataKey="name" type="category" width={60} axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 12, fontWeight: 500}} />
                <Tooltip cursor={{fill: '#f8fafc'}} contentStyle={{borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)'}} />
                <Bar dataKey="value" radius={[0, 8, 8, 0]} barSize={24} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* AI Insights & Quick Stats */}
        <div className="flex flex-col gap-4">
          <div className="bg-gradient-to-br from-emerald-500 to-teal-600 rounded-3xl p-6 text-white shadow-md shadow-emerald-500/20">
            <h3 className="text-lg font-semibold mb-2 flex items-center gap-2">
              <Award className="text-emerald-100" /> AI Coach Insight
            </h3>
            <p className="text-emerald-50 font-medium leading-relaxed">
              You've kept sugar under 15g for 3 days straight! Keep it up. Need a healthy snack? Try Greek yogurt with almonds.
            </p>
          </div>
          
          <div className="bg-white rounded-3xl p-6 shadow-sm border border-slate-100 flex-1">
             <h3 className="text-sm font-semibold text-slate-500 uppercase tracking-wider mb-2">Calories</h3>
             <div className="flex items-end gap-2">
               <span className="text-3xl font-black text-slate-800">1,450</span>
               <span className="text-slate-500 mb-1 font-medium">/ 2,000 kcal</span>
             </div>
             <div className="w-full bg-slate-100 h-3 rounded-full mt-4 overflow-hidden">
               <div className="bg-amber-500 h-full rounded-full" style={{ width: '72%' }}></div>
             </div>
          </div>
        </div>
      </div>

      {/* Weekly Trends */}
      <div className="bg-white rounded-3xl p-6 shadow-sm border border-slate-100">
        <h3 className="text-lg font-semibold text-slate-700 mb-6 flex items-center gap-2">
          <TrendingUp className="text-indigo-500" /> Weekly Health Trend
        </h3>
        <div className="h-64 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={weeklyTrends}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
              <XAxis dataKey="day" axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 12, fontWeight: 500}} dy={10} />
              <YAxis hide domain={[0, 100]} />
              <Tooltip cursor={{fill: '#f1f5f9'}} contentStyle={{borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)'}} />
              <Bar dataKey="score" fill="#10b981" radius={[8, 8, 0, 0]} barSize={40}>
                {weeklyTrends.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.score > 80 ? '#10b981' : '#f59e0b'} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
