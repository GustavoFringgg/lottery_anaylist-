const WEEKDAYS = ["一", "二", "三", "四", "五", "六", "日"]

export const formatDate = (iso: string) => {
  const d = new Date(iso)
  const roc = d.getFullYear() - 1911
  const mm = String(d.getMonth() + 1).padStart(2, "0")
  const dd = String(d.getDate()).padStart(2, "0")
  const hh = String(d.getHours()).padStart(2, "0")
  const min = String(d.getMinutes()).padStart(2, "0")
  const weekday = WEEKDAYS[d.getDay() === 0 ? 6 : d.getDay() - 1]
  return {
    date: `${roc}/${mm}/${dd}(${weekday})`,
    time: `${hh}:${min}`
  }
}
