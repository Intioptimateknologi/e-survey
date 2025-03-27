type ChartData = {
  date: string;
  count: number;
};

type DashboardResponse = {
  success: boolean;
  message: string;
  data: {
    surveys: number;
    respondents: number;
    users: {
      admin: number;
      member: number;
      total: number;
    };
  };
  chart: {
    member_registration: ChartData[];
    respondent_filling: ChartData[];
    survey_creation: ChartData[];
  };
};
