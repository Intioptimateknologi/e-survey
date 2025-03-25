export function formatDateTimeLocal(isoString: String) {
  if (!isoString) return "";
  return isoString.slice(0, 16);
}
