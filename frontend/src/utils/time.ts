import { format } from "date-fns";
import { id as localeId } from "date-fns/locale";

export function formatDateTimeLocal(isoString: String) {
  if (!isoString) return "";
  return isoString.slice(0, 16);
}

export function getTime(time: string) {
  return format(new Date(time), "dd MMMM yyyy HH:mm", { locale: localeId });
}
